import numpy as np
import cv2 as cv
import asyncio

from WindowCapture import WindowCapture


JPEG_QUALITY = 70
PNG_QUALITY = 50


class AsyncWindowRender:
    def __init__(self, window_name: str) -> None:
        self.wincap = WindowCapture(window_name)
        asyncio.run(self.main())

    async def create_frame(self) -> np.ndarray:
        frame = self.wincap.get_screenshot()
        return frame

    async def build_frame(self):
        while True:

            cv.imshow('Computer Vision', await self.create_frame())
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                raise

    async def main(self):
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.create_frame())
            tg.create_task(self.build_frame())

# if __name__ == '__main__':
#    asyncio.run(main())
