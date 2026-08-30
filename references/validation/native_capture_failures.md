# Native capture failures

The first OS client capture used ImageGrab and failed with `OSError: screen grab failed` in each capture thread. The second attempt captured six black front-buffer images at 1280×800 pixels (3,057 bytes each). They were actually inspected and rejected; copies remain ignored under `outputs/failed_front_capture`.

The third method captured the actual drawn OpenGL back buffer immediately before the original window flip. All six frames were inspected and accepted. No scene was recreated and no task input was overridden for capture. This establishes rendering, not physical monitor scanout, OS keyboard submission or IME behavior. Failed attempts are not counted as visual passes.
