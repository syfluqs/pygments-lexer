# -*- coding: utf-8 -*-
"""
    pygments.lexers.m4pic
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for M4 Pic.

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

__all__ = ['M4PicLexer']

####################################################################################################

class M4PicLexer(RegexLexer):
    """ For M4-Pic source code. """
    name = 'm4pic'
    aliases = ['m4pic',]
    filenames = ['*.m4']
    mimetypes = ['text']
    flags = re.MULTILINE

    gnu_m4_macros = (
	'__file__',
	'__gnu__',
	'__line__',
	'__os2__',
	'__program__',
	'__unix__',
	'__windows__',
	'argn',
	'array',
	'array_set',
	'builtin',
	'capitalize',
	'changecom',
	'changequote',
	'changeword',
	'cleardivert',
	'cond',
	'copy',
	'curry',
	'debugfile',
	'debugmode',
	'decr',
	'define',
	'define_blind',
	'defn',
	'divert',
	'divnum',
	'dnl',
	'downcase',
	'dquote',
	'dquote_elt',
	'dumpdef',
	'errprint',
	'esyscmd',
	'eval',
	'example',
	'exch',
	'fatal_error',
	'foreach',
	'foreachq',
	'forloop',
	'format',
	'ifdef',
	'ifelse',
	'ifelse',
	'ifelse',
	'include',
	'incr',
	'index',
	'indir',
	'join',
	'joinall',
	'len',
	'm4exit',
	'm4wrap',
	'maketemp',
	'mkstemp',
	'nargs',
	'os2',
	'patsubst',
	'popdef',
	'pushdef',
	'quote',
	'regexp',
	'rename',
	'reverse',
	'shift',
	'sinclude',
	'stack_foreach',
	'stack_foreach_lifo',
	'stack_foreach_sep',
	'stack_foreach_sep_lifo',
	'substr',
	'syscmd',
	'sysval',
	'traceoff',
	'traceon',
	'translit',
	'undefine',
	'undivert',
	'unix',
	'upcase',
	'windows',
        )


    tokens = {
        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'#.*', Comment.Single),
            ],
        'root': [
            include('whitespace'),
            (r'[(){},;:."\']', Punctuation),
            ('(\))(dnl)', bygroups(Punctuation, Keyword)),
            (r'[=+\-\*\/]', Operator),
            #
            (r'`', String, 'string'),
            #
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+', Number.Float),
            (r'(\d+\.\d*|\.\d+)', Number.Float),
            (r'\d+', Number.Integer),
            (r'\$\d', Name.Variable),
            ('(' + '|'.join(gnu_m4_macros) + ')', Name.Builtin),
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
            ],
        'string': [
            (r"[^`']", String),
            (r"`", String, '#push'),
            (r"'", String, '#pop'),
        ],
    }

####################################################################################################
# 
# End
# 
####################################################################################################
