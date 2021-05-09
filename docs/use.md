# Example Usage

Folders with even different files (not present in the other folder):
```
$ python -m subtractor tests/fixtures/different/{ref,obs}
2021-05-09T22:36:45.960 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/different/ref and future=tests/fixtures/different/obs in folder mode
2021-05-09T22:36:45.960 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/_a.png, obs=None
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_green_and_blue.png, obs=None
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=None, obs=tests/fixtures/different/obs/bright_red_green_or_blue_dunno.png
2021-05-09T22:36:45.961 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_half_transparent.png, obs=tests/fixtures/different/obs/bright_red_half_transparent.png
2021-05-09T22:36:45.961 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:36:45.962 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:36:45.962 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:36:45.964 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:36:45.991 INFO [subtractor]:   Match of obs=tests/fixtures/different/obs/bright_red_half_transparent.png
2021-05-09T22:36:45.992 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_or_blue.png, obs=tests/fixtures/different/obs/bright_red_or_blue.png
2021-05-09T22:36:45.992 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:36:45.992 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.992 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:36:45.993 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.995 INFO [subtractor]:   Mismatch of obs=tests/fixtures/different/obs/bright_red_or_blue.png is 100 of 100 pixels or 100.0 %
2021-05-09T22:36:45.995 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/bright_red_or_green_dunno.png, obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png
2021-05-09T22:36:45.995 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/bright_red_or_green_dunno.png to be OK with size 276 bytes
2021-05-09T22:36:45.996 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.996 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png to be OK with size 6245 bytes
2021-05-09T22:36:45.997 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:36:45.998 INFO [subtractor]:   Mismatch of obs=tests/fixtures/different/obs/bright_red_or_green_dunno.png is 20 of 100 pixels or 20.0 %
2021-05-09T22:36:45.998 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/negative_strip.png, obs=tests/fixtures/different/obs/negative_strip.png
2021-05-09T22:36:45.998 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/negative_strip.png to be OK with size 38574 bytes
2021-05-09T22:36:45.999 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/negative_strip.png as PNG to be OK with shape 1920x1080
2021-05-09T22:36:45.999 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/negative_strip.png to be OK with size 38574 bytes
2021-05-09T22:36:46.000 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/negative_strip.png as PNG to be OK with shape 1920x1080
2021-05-09T22:36:49.076 INFO [subtractor]:   Match of obs=tests/fixtures/different/obs/negative_strip.png
2021-05-09T22:36:49.076 INFO [subtractor]: Pair ref=tests/fixtures/different/ref/something_else.png, obs=tests/fixtures/different/obs/something_else.png
2021-05-09T22:36:49.076 INFO [subtractor]:   Found ref=tests/fixtures/different/ref/something_else.png to be OK with size 540 bytes
2021-05-09T22:36:49.078 INFO [subtractor]:     Analyzed ref=tests/fixtures/different/ref/something_else.png as PNG to be OK with shape 1920x1080
2021-05-09T22:36:49.078 INFO [subtractor]:   Found obs=tests/fixtures/different/obs/something_else.png to be OK with size 38574 bytes
2021-05-09T22:36:49.079 INFO [subtractor]:     Analyzed obs=tests/fixtures/different/obs/something_else.png as PNG to be OK with shape 1920x1080
2021-05-09T22:37:07.103 INFO [subtractor]:   Mismatch of obs=tests/fixtures/different/obs/something_else.png is 1369324 of 2073600 pixels or 66.0 %
2021-05-09T22:37:07.103 INFO [subtractor]: Pair ref=None, obs=tests/fixtures/different/obs/z.png
2021-05-09T22:37:07.103 INFO [subtractor]: Pair ref=None, obs=tests/fixtures/different/obs/zz.png
2021-05-09T22:37:07.103 INFO [subtractor]: Finished comparisons finding good=2 and bad=8 in folder mode
FAIL
```

Folders with deviating files (same number of files with matching names):
```
$ python -m subtractor tests/fixtures/deviating/{ref,obs}
2021-05-09T22:38:14.227 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/deviating/ref and future=tests/fixtures/deviating/obs in folder mode
2021-05-09T22:38:14.228 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:38:14.228 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png, obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png
2021-05-09T22:38:14.228 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:38:14.229 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:38:14.229 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png to be OK with size 290 bytes
2021-05-09T22:38:14.231 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png as PNG to be OK with shape 2x2
2021-05-09T22:38:14.266 INFO [subtractor]:   Match of obs=tests/fixtures/deviating/obs/bright_red_half_transparent.png
2021-05-09T22:38:14.266 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_or_blue.png, obs=tests/fixtures/deviating/obs/bright_red_or_blue.png
2021-05-09T22:38:14.266 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:38:14.268 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.268 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_or_blue.png to be OK with size 276 bytes
2021-05-09T22:38:14.269 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_or_blue.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.272 INFO [subtractor]:   Mismatch of obs=tests/fixtures/deviating/obs/bright_red_or_blue.png is 100 of 100 pixels or 100.0 %
2021-05-09T22:38:14.272 INFO [subtractor]: Pair ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png, obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png
2021-05-09T22:38:14.272 INFO [subtractor]:   Found ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png to be OK with size 276 bytes
2021-05-09T22:38:14.273 INFO [subtractor]:     Analyzed ref=tests/fixtures/deviating/ref/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.273 INFO [subtractor]:   Found obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png to be OK with size 6245 bytes
2021-05-09T22:38:14.275 INFO [subtractor]:     Analyzed obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png as PNG to be OK with shape 10x10
2021-05-09T22:38:14.277 INFO [subtractor]:   Mismatch of obs=tests/fixtures/deviating/obs/bright_red_or_green_dunno.png is 20 of 100 pixels or 20.0 %
2021-05-09T22:38:14.277 INFO [subtractor]: Finished comparisons finding good=1 and bad=2 in folder mode
FAIL
```

Folders with identical files:
```
$ python -m subtractor tests/fixtures/ref_obs/{ref,obs}
2021-05-09T22:39:05.954 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/ref_obs/ref and future=tests/fixtures/ref_obs/obs in folder mode
2021-05-09T22:39:05.954 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:39:05.955 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png, obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:05.955 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:05.957 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:05.957 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:05.958 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:05.993 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:05.994 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png, obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:05.994 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:05.996 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:05.996 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:06.006 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:06.007 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:06.008 INFO [subtractor]: Finished comparisons finding good=2 and bad=0 in folder mode
OK
```

Same with debug mode:
```
$ SUBTRACTOR_DEBUG=1 python -m subtractor tests/fixtures/ref_obs/{ref,obs}
2021-05-09T22:39:51.410 DEBUG [subtractor]: Guarded dispatch forest=['tests/fixtures/ref_obs/ref', 'tests/fixtures/ref_obs/obs']
2021-05-09T22:39:51.410 DEBUG [subtractor]: Timeline past=tests/fixtures/ref_obs/ref, present=tests/fixtures/ref_obs/diff-of-ref_obs, and future=tests/fixtures/ref_obs/obs
2021-05-09T22:39:51.410 INFO [subtractor]: Starting comparisons visiting past=tests/fixtures/ref_obs/ref and future=tests/fixtures/ref_obs/obs in folder mode
2021-05-09T22:39:51.410 INFO [subtractor]:   Threshold for pixel mismatch is 1 %
2021-05-09T22:39:51.411 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png, obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:51.411 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:51.413 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.413 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png to be OK with size 277 bytes
2021-05-09T22:39:51.415 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.462 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 119 1
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: b'bKGD' 119 1 (unknown)
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 132 7
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: b'tIME' 132 7 (unknown)
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 151 12
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.463 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 119 1
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: b'bKGD' 119 1 (unknown)
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 132 7
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: b'tIME' 132 7 (unknown)
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 151 12
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 175 37
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 224 37
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 175 37
2021-05-09T22:39:51.464 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 224 37
2021-05-09T22:39:51.467 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/ff0000_2x2.png
2021-05-09T22:39:51.467 INFO [subtractor]: Pair ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png, obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:51.467 INFO [subtractor]:   Found ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:51.468 INFO [subtractor]:     Analyzed ref=tests/fixtures/ref_obs/ref/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.468 INFO [subtractor]:   Found obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png to be OK with size 290 bytes
2021-05-09T22:39:51.470 INFO [subtractor]:     Analyzed obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png as PNG to be OK with shape 2x2
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'tRNS' 119 1
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 132 1
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: b'bKGD' 132 1 (unknown)
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 145 7
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: b'tIME' 145 7 (unknown)
2021-05-09T22:39:51.470 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 164 12
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'IHDR' 16 13
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'gAMA' 41 4
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'cHRM' 57 32
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'PLTE' 101 6
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tRNS' 119 1
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'bKGD' 132 1
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: b'bKGD' 132 1 (unknown)
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tIME' 145 7
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: b'tIME' 145 7 (unknown)
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'IDAT' 164 12
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 188 37
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 237 37
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 188 37
2021-05-09T22:39:51.471 DEBUG [PIL.PngImagePlugin]: STREAM b'tEXt' 237 37
2021-05-09T22:39:51.473 INFO [subtractor]:   Match of obs=tests/fixtures/ref_obs/obs/rgba_255-0-0-0.5_2x2.png
2021-05-09T22:39:51.473 INFO [subtractor]: Finished comparisons finding good=2 and bad=0 in folder mode
OK
```
