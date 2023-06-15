import time
import atexit
import customtkinter as ctk
import threading

from GUI.selectField import SelectField
from SyncStream import Stream
from AsyncWindowRender import AsyncWindowRender

HEIGHT = 600
WIDTH = 800


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.stream: Stream
        self.async_window_render: AsyncWindowRender

        ctk.set_appearance_mode('blue')
        ctk.set_default_color_theme('dark-blue')

        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.window_select_field: SelectField = SelectField(self,)
        self.window_select_field.place(x=175, y=100, )

        self.check_captured_window: ctk.CTkButton = ctk.CTkButton(
            self, text="Check captured window", command=self.check_captured_window_clicked, )
        self.check_captured_window.pack()
        self.check_captured_window.place(x=200, y=450)

        self.stream_start_button: ctk.CTkButton = ctk.CTkButton(
            self, text="Start stream", command=self.stream_start_button_clicked, )
        self.stream_start_button.pack()
        self.stream_start_button.place(x=500, y=450)

        self.stream_stop_button: ctk.CTkButton = ctk.CTkButton(
            self, text="Stop stream", command=self.stream_stop_button_clicked, state=ctk.DISABLED)
        self.stream_stop_button.pack()
        self.stream_stop_button.place(x=500, y=500)

        self.url_link_field = ctk.CTkEntry(
            self, placeholder_text="URL-link", width=500, )
        self.url_link_field.insert(0, 'rtsp://localhost:8554/s')
        self.url_link_field.pack()
        self.url_link_field.place(x=175, y=400)

        self.mainloop()

    def check_captured_window_clicked(self):
        window_name: str = self.window_select_field.get()
        self.async_window_render = AsyncWindowRender(
            window_name=window_name)  # display captured window

    # TODO: create separate thread for checking stream.ffmpeg.stderr ->
    # cause if it's empty, it would block, all program,
    # after implementig it, refactor ->
    # stream.produce_frame try except block

    # def stderr_handler(self):
    #    print(self.stream.ffmpeg.stderr.read().decode('utf-8'))

    def stream_start_button_clicked(self):

        window_name: str = self.window_select_field.get()
        url = self.url_link_field.get()
        self.stream = Stream(window_name=window_name, url=url)

        self.stream.stream_thread.start()
        time.sleep(0.1)  # important pause need to be cause creating hwnd

        if self.stream.stop_event.is_set():
            self.stream.stop_stream()
        else:
            self.stream_start_button.configure(state=ctk.DISABLED)
            self.stream_stop_button.configure(state=ctk.NORMAL)

    def stream_stop_button_clicked(self):
        self.stream.stop_stream()
        if self.stream.stop_event.is_set():
            self.stream_start_button.configure(state=ctk.NORMAL)
            self.stream_stop_button.configure(state=ctk.DISABLED)


if __name__ == '__main__':
    app = App()
