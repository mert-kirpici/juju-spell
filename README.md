# Juju Machine Exporter

multijuju snap collects machines' running status in all models under a Juju controller. It also provides an interface to
expose the metrics to Prometheus for storage and further usage.

## Deployment

To get the latest stable version of the snap from Snapstore, run:

```bash
sudo snap install multijuju
```

To get the latest development version of the snap, build from the source code and install with `--dangerous` flag:

```bash
make build
sudo snap install --dangerous multijuju.snap
```
