# Important Notice

The astropy conda channel is no longer active. Please pull Astropy Project packages from
`conda-forge` channel instead if you must use `conda` but we recommend `pip` where possible.

# For users

To install the conda packages maintained in this repository do
`conda install -c astropy package_name`

If you use this channel frequently it may be convenient to add the conda
channel for this repository to your list of default channels:

```
conda config --add channels astropy
```

# For maintainers/contributors

[![Build Status](https://travis-ci.org/astropy/conda-channel-astropy.svg?branch=main)](https://travis-ci.org/astropy/conda-channel-astropy)

## Dependencies

This packages uses the file `sync.py` from https://github.com/glue-viz/conda-sync to copy packages from the conda-forge channel to the astropy channel.

## Updating an existing package to a new version

Update the package on conda-forge. Once a day a cron job is run to copy packages over to this channel. If an immediate copy is needed, push an empty commit to main.

## Adding a new package

Add the package on conda-forge, then add it to the file `requirements.yml` in this repository.

## In case of emergency, copy manually

First install `anaconda-client`. Once you have done that, use it to log in to anaconda at
the command line:

```
$ anaconda login
```

Once you are logged in you can do the copy from the command line:

```
$ anaconda copy --to-owner astropy conda-forge/astroquery/0.3.9
```

If you want to copy just one specific file from conda-forge add its name after
the version number. See `anaconda copy --help` for details.
