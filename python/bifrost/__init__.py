
# Copyright (c) 2016-2022, The Bifrost Authors. All rights reserved.
# Copyright (c) 2016, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of The Bifrost Authors nor the names of its
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Bifrost pipeline processing library
"""

# TODO: Decide how to organise the namespace
from __future__ import print_function, absolute_import

from bifrost import core, memory, affinity, ring, block, address, udp_socket
from bifrost import pipeline
from bifrost import device
from bifrost.ndarray import ndarray, asarray, empty_like, empty, zeros_like, zeros
from bifrost import views
from bifrost.map import map, clear_map_cache, list_map_cache
from bifrost.pipeline import Pipeline, get_default_pipeline, block_scope
from bifrost import blocks
from bifrost.block_chainer import BlockChainer
from bifrost.reduce import reduce
# import copy_block, transpose_block, scrunch_block, sigproc_block, fdmt_block
from bifrost.transpose import transpose
from bifrost.unpack import unpack
from bifrost.quantize import quantize

try:
    from bifrost.version import __version__
except ImportError:
    print("*************************************************************************")
    print("Please run `configure` and `make` from the root of the source tree to")
    print("generate the bifrost.version module.")
    print("*************************************************************************")
    raise
__author__     = "The Bifrost Authors"
__copyright__  = "Copyright (c) 2016-2020, The Bifrost Authors. All rights reserved.\nCopyright (c) 2016, NVIDIA CORPORATION. All rights reserved."
__credits__    = ["Ben Barsdell"]
__license__    = "BSD 3-Clause"
__maintainer__ = "Ben Barsdell"
__email__      = "benbarsdell@gmail.com"
__status__     = "Development"
