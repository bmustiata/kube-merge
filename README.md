kube-merge allows merging other Kubernetes configurations into the
current configuration.

Installation
============

    pip install kube-merge

Usage
=====

In order to merge other configs first dump the configuration to a file.
For example if using the microk8s snap from Ubuntu, just dump the
configuration to a file:

    microk8s.kubectl config view --raw > microk8s.yml

then simply add it:

    kube-merge microk8s.yml

This *will change* the default configuration, adding the clusters and
users.

From there you’ll just switch the context using the regular:

    kubectl config use-context ...
