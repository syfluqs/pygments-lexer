# -*- coding: utf-8 -*-
"""
    pygments.lexers.spice
    ~~~~~~~~~~~~~~~~~~~~

    Lexers for Spice.

    :copyright: Copyright 2013 Fabrice Salvaire.
    :license: BSD, see LICENSE for details.
"""

####################################################################################################

import re
from pygments.lexer import RegexLexer, bygroups, include, using, this
from pygments.token import (
    Text, Comment, Operator, Keyword, Name, String, Number, Punctuation,
    )

####################################################################################################

#     Token:                         '',
# 
#     Text:                          '',
#     Whitespace:                    'w',
#     Error:                         'err',
#     Other:                         'x',
# 
#     Keyword:                       'k',
#     Keyword.Constant:              'kc',
#     Keyword.Declaration:           'kd',
#     Keyword.Namespace:             'kn',
#     Keyword.Pseudo:                'kp',
#     Keyword.Reserved:              'kr',
#     Keyword.Type:                  'kt',
# 
#     Name:                          'n',
#     Name.Attribute:                'na',
#     Name.Builtin:                  'nb',
#     Name.Builtin.Pseudo:           'bp',
#     Name.Class:                    'nc',
#     Name.Constant:                 'no',
#     Name.Decorator:                'nd',
#     Name.Entity:                   'ni',
#     Name.Exception:                'ne',
#     Name.Function:                 'nf',
#     Name.Property:                 'py',
#     Name.Label:                    'nl',
#     Name.Namespace:                'nn',
#     Name.Other:                    'nx',
#     Name.Tag:                      'nt',
#     Name.Variable:                 'nv',
#     Name.Variable.Class:           'vc',
#     Name.Variable.Global:          'vg',
#     Name.Variable.Instance:        'vi',
# 
#     Literal:                       'l',
#     Literal.Date:                  'ld',
# 
#     String:                        's',
#     String.Backtick:               'sb',
#     String.Char:                   'sc',
#     String.Doc:                    'sd',
#     String.Double:                 's2',
#     String.Escape:                 'se',
#     String.Heredoc:                'sh',
#     String.Interpol:               'si',
#     String.Other:                  'sx',
#     String.Regex:                  'sr',
#     String.Single:                 's1',
#     String.Symbol:                 'ss',
# 
#     Number:                        'm',
#     Number.Float:                  'mf',
#     Number.Hex:                    'mh',
#     Number.Integer:                'mi',
#     Number.Integer.Long:           'il',
#     Number.Oct:                    'mo',
# 
#     Operator:                      'o',
#     Operator.Word:                 'ow',
# 
#     Punctuation:                   'p',
# 
#     Comment:                       'c',
#     Comment.Multiline:             'cm',
#     Comment.Preproc:               'cp',
#     Comment.Single:                'c1',
#     Comment.Special:               'cs',
# 
#     Generic:                       'g',
#     Generic.Deleted:               'gd',
#     Generic.Emph:                  'ge',
#     Generic.Error:                 'gr',
#     Generic.Heading:               'gh',
#     Generic.Inserted:              'gi',
#     Generic.Output:                'go',
#     Generic.Prompt:                'gp',
#     Generic.Strong:                'gs',
#     Generic.Subheading:            'gu',
#     Generic.Traceback:             'gt',

####################################################################################################

__all__ = ['SpiceLexer']

####################################################################################################

class SpiceLexer(RegexLexer):
    """ For Spice source code. """
    name = 'spice'
    aliases = ['spice',]
    filenames = ['*.cir']
    mimetypes = ['text/x-spice']
    flags = re.MULTILINE | re.IGNORECASE

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text), # line continuation
            (r'^\*.*', Comment.Single),
            (r'[(){}]', Punctuation),
            (r'[=+\-\*\/]', Operator),
            (r'^(x|R|C|D|V)[a-z0-9]+', Name.Attribute),
            #(r'^(\.include)(\s)(.*)$', bygroups(Keyword, Text.Whitespace, String)),
            include('directives'),
            (r'[0-9][a-zA-Z_\.][a-zA-Z0-9_\.]*', Name),
            (r'[a-zA-Z_][a-zA-Z0-9_\.]*', Name),
            include('numbers'),
            ],
        'directives': [
            (r'^\.('
             r'control|endc|'
             r'title|end|'
             r'options|param|'
             r'model|'
             r'subckt|ends|'
             r'include|'
             r'op|tran|'
             r'save|'
             ')', Keyword),
            ],
        'numbers': [
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+', Number.Float),
            (r'(\d+\.\d*|\.\d+)', Number.Float),
            (r'\d+', Number.Integer),
            ],
    }

####################################################################################################
# 
# End
# 
####################################################################################################
