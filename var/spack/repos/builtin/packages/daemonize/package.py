# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Daemonize(Package):
    """The Emacs programmable text editor."""

    homepage = "https://software.clapper.org/daemonize"
    url = "https://github.com/bmc/daemonize/archive/refs/tags/release-1.7.8.tar.gz"
    git = "https://github.com/bmc/daemonize.git"

    maintainers("vmiheer")

    version("master", branch="master")
    version("1.7.8", sha256="20c4fc9925371d1ddf1b57947f8fb93e2036eb9ccc3b43a1e3678ea8471c4c60")

    depends_on("c", type="build")  # generated
    depends_on("gmake", type="build")

    def install(self, spec, prefix):
        configure("--prefix={0}".format(prefix))
        make()
        make("install")
