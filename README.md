# My_TRexFitter

Config collections of TRexFitter

## Set up docker

1. log in

    ```bash
    docker login gitlab-registry.cern.ch
    ```

2. pull image

    ```bash
    docker pull gitlab-registry.cern.ch/trexstats/trexfitter:latest
    ```

## Start docker

- Windows

```bash
. docker/start_TRexFitter.bat
```

- gpuatum02

```bash
source docker/start_TRexFitter_gpuatum02.sh
```

## Reference

- gitlab: <https://gitlab.cern.ch/TRExStats/TRExFitter>
