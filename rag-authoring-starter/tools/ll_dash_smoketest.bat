@echo off
setlocal enabledelayedexpansion
set FFMPEG="C:\Users\tsto\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0-full_build\bin\ffmpeg.exe"
set OUT=%TEMP%\dashif-ll-smoketest
if not exist "%OUT%" mkdir "%OUT%"

%FFMPEG% -hide_banner -y ^
  -f lavfi -i "testsrc2=size=640x360:rate=25" ^
  -f lavfi -i "sine=frequency=1000:sample_rate=48000" ^
  -t 4 ^
  -c:v libx264 -tune zerolatency -g 25 -keyint_min 25 -sc_threshold 0 -b:v 800k -pix_fmt yuv420p ^
  -c:a aac -b:a 128k -ac 2 ^
  -use_template 1 ^
  -use_timeline 1 ^
  -utc_timing_url "https://time.akamai.com/?iso" ^
  -format_options "movflags=cmaf" ^
  -adaptation_sets "id=0,streams=v id=1,streams=a" ^
  -seg_duration 1.5 ^
  -frag_duration 0.5 ^
  -frag_type duration ^
  -streaming 1 ^
  -ldash 1 ^
  -write_prft 1 ^
  -target_latency 3.5 ^
  -f dash "%OUT%\out.mpd"

set RC=%ERRORLEVEL%
echo.
echo === ffmpeg exit code: %RC% ===
if exist "%OUT%\out.mpd" (
  echo Manifest created: "%OUT%\out.mpd"
  dir /b "%OUT%"
) else (
  echo NO MANIFEST PRODUCED
)
exit /b %RC%