# streaming-with-python
A small python project that create stream, by screenshotting captured window and feeding it to ffmpeg. Want to add sound capturing
, in far future, want to create streaming platform. 

NOW SUPPORT ONLY RTSP STREAMING (hardcoded)

# Quick start
  1. Clone a project
```
git clone https://github.com/ririol/streaming-with-python.git
```
  2. Install dependencies
```
$ pip install -r requirements.txt
$ .\build-example.sh
```
  3. Also you have to install rtsp server, and ffmpeg 
    - [ffmpeg](https://ffmpeg.org/)
    - In my case I used [MediaMTX](https://github.com/bluenviron/mediamtx) 


# Roadmap

- [x] Video capturing
- [x] Minimal interface
- [ ] Audio capturing
- [ ] Stream settings interface 
- [ ] My streaming platform
- [ ] OS support
    - [ ] Linux
    - [ ] MacOS

# Acknowledgments
  - https://ffmpeg.org/
  - https://github.com/bluenviron/mediamtx
  - [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)
