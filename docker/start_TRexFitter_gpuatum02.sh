docker run -it --rm \
    -v $(git rev-parse --show-toplevel):/work \
    -v /net/s3_datae/yangz:/data \
    -w /work \
    gitlab-registry.cern.ch/trexstats/trexfitter:latest
