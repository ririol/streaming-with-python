import pygetwindow
# import win32gui #not usable


def get_list_of_top_windows() -> list[str]:
    windows = pygetwindow.getAllWindows()
    window_list = []
    for window in windows:
        if window.title:
            window_list.append(window.title)

    window_list.append('')
    window_list.sort()

    return window_list


if __name__ == '__main__':
    window_list = get_list_of_top_windows()
    for i in window_list:
        print(i)
