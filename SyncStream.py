import ffmpeg
import subprocess
import threading

from WindowCapture import WindowCapture


class Stream():
    def __init__(self, window_name: str, url: str) -> None:

        self.wincap = WindowCapture(window_name)
        self.url: str = url
        self.stream_thread = threading.Thread(target=self.start_stream)
        self.stop_event = threading.Event()

        self.ffmpeg: subprocess.Popen = self.init_ffmpeg_process()
        self.audio: subprocess.Popen

    # TODO: implement builder pattern (or fabric) for creating stream video settings
    def init_ffmpeg_process(self) -> subprocess.Popen:
        process: subprocess.Popen = (
            ffmpeg
            .input('pipe:', format='rawvideo', pix_fmt='rgba', s=f'{self.wincap.w}x{self.wincap.h}', framerate=90, )
            .output(
                self.url,
                listen=1,
                f='rtsp',
                codec='h264_nvenc',
                framerate=60,
                # panic fatal error info debug trace (info default)
                loglevel='info',
                rtsp_transport='tcp',
            )

            .global_args('-hide_banner', '-threads', '8', '-re')
            .run_async(pipe_stdin=True, pipe_stderr=True)
        )

        return process

    # TODO: change try except by stderr_handler in new thread

    def produce_frame(self):
        # try:
        frame = self.wincap.get_screenshot()
        self.ffmpeg.stdin.write(frame.tobytes())  # type: ignore
        # except Exception:
        #    self.stop_event.set()

    # TODO: FPS cap

    def start_stream(self):
        while not self.stop_event.is_set():
            self.produce_frame()

    def stop_stream(self):
        self.stop_event.set()
        self.ffmpeg.stdin.close()  # type: ignore
        self.ffmpeg.kill()


if __name__ == '__main__':
    from utils.get_windows import get_list_of_top_windows

    def main(window_name: str):
        stream = Stream(window_name,  url='   ')

        stream.start_stream()

    windows_list = get_list_of_top_windows()
    for i, window in enumerate(windows_list):
        print(i+1, window)

    main(windows_list[int(input())-1],)
