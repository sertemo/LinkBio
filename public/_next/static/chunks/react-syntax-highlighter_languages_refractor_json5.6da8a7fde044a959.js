"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[22180,43657],{45950:function(n){function json(n){n.languages.json={property:{pattern:/(^|[^\\])"(?:\\.|[^\\"\r\n])*"(?=\s*:)/,lookbehind:!0,greedy:!0},string:{pattern:/(^|[^\\])"(?:\\.|[^\\"\r\n])*"(?!\s*:)/,lookbehind:!0,greedy:!0},comment:{pattern:/\/\/.*|\/\*[\s\S]*?(?:\*\/|$)/,greedy:!0},number:/-?\b\d+(?:\.\d+)?(?:e[+-]?\d+)?\b/i,punctuation:/[{}[\],]/,operator:/:/,boolean:/\b(?:false|true)\b/,null:{pattern:/\bnull\b/,alias:"keyword"}},n.languages.webmanifest=n.languages.json}n.exports=json,json.displayName="json",json.aliases=["webmanifest"]},50235:function(n,e,s){var a=s(45950);function json5(n){var e;n.register(a),e=/("|')(?:\\(?:\r\n?|\n|.)|(?!\1)[^\\\r\n])*\1/,n.languages.json5=n.languages.extend("json",{property:[{pattern:RegExp(e.source+"(?=\\s*:)"),greedy:!0},{pattern:/(?!\s)[_$a-zA-Z\xA0-\uFFFF](?:(?!\s)[$\w\xA0-\uFFFF])*(?=\s*:)/,alias:"unquoted"}],string:{pattern:e,greedy:!0},number:/[+-]?\b(?:NaN|Infinity|0x[a-fA-F\d]+)\b|[+-]?(?:\b\d+(?:\.\d*)?|\B\.\d+)(?:[eE][+-]?\d+\b)?/})}n.exports=json5,json5.displayName="json5",json5.aliases=[]}}]);