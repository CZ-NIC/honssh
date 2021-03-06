# Copyright (c) 2015 Robert Putt (http://www.github.com/robputt796)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The names of the author(s) may not be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHORS ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

from twisted.python import log

def validate_containers_config(cfg):
    log.msg('[PLUGIN:CONTAINERS] Checking for containers configuration')
    cfgvalid = True

    if cfg.get('containers','enabled') == 'true':
        props = [['containers','driver'], ['containers','image'], ['containers','uri'], ['containers','launch_cmd'], ['containers','hostname']]
        for prop in props:
            if not checkExist(cfg,prop):
                cfgvalid = False

    return cfgvalid

def checkExist(cfg, property): 
    if cfg.has_option(property[0], property[1]):   
        if not cfg.get(property[0], property[1]) == '':
            return True
        else:
            print '[VALIDATION] - [' + property[0] + '][' + property[1] + '] must not be blank.'
            return False
    else:
        print '[VALIDATION] - [' + property[0] + '][' + property[1] + '] must exist.'
        return False
