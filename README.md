# re3 RPM packages for Fedora/Ultramarine/CentOS/Nobara

This repository contains Andaman and RPM specs for re3, the re-implementation of the RenderWare GTA games. It contains build for GTA III and Vice City.

Liberty City Stories and Vice City Stories are not supported at this time because I cannot test them from the PSP/PS2 ROMs.

## Building

1. Add [Terra](https://terra.fyralabs.com) to your system.
2. Install Andaman
   ```
   sudo dnf install anda mock rpm-build
   ```
3. Clone this repository
4. Run `anda build <project>` where `<project>` is the name of the subproject we want to build. For example, to build reVC, run `anda build revc`.

## Installing

1. Build the package using the instructions above.
2. Andaman should tell you it has built a packaged somewhere in `anda-build`, simply install it using `sudo dnf install <path-to-rpm>`.
3. Install the game data from your original copy of the game inside `~/.reVC` or `~/.re3` depending on the game you are installing.
4. Replace extra files from `/usr/share/reVC` or `/usr/share/re3` to `~/.reVC` or `~/.re3` respectively.
   ```
   cp -av /usr/share/reVC/* ~/.reVC # or ~/.re3
   ```

Now you should be able to run the game by opening the desktop entry. If you'd like to run it from the terminal you must enter the game directory and run the `reVC` or `re3` binary since re3 looks for the game data in the current working directory.

## License

re3 is unlicensed software due to the nature of the project. All rights are reserved to the original authors. The RPM spec files are licensed under the WTFPL.
Do what you will.