(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[82023,67417],{82023:function(e,t,r){"use strict";var n=r(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var o=n(r(27536)).default;t.default=o},27536:function(e){"use strict";function tremor(e){var t;e.languages.tremor={comment:{pattern:/(^|[^\\])(?:\/\*[\s\S]*?\*\/|(?:--|\/\/|#).*)/,lookbehind:!0},"interpolated-string":null,extractor:{pattern:/\b[a-z_]\w*\|(?:[^\r\n\\|]|\\(?:\r\n|[\s\S]))*\|/i,greedy:!0,inside:{regex:{pattern:/(^re)\|[\s\S]+/,lookbehind:!0},function:/^\w+/,value:/\|[\s\S]+/}},identifier:{pattern:/`[^`]*`/,greedy:!0},function:/\b[a-z_]\w*(?=\s*(?:::\s*<|\())\b/,keyword:/\b(?:args|as|by|case|config|connect|connector|const|copy|create|default|define|deploy|drop|each|emit|end|erase|event|flow|fn|for|from|group|having|insert|into|intrinsic|let|links|match|merge|mod|move|of|operator|patch|pipeline|recur|script|select|set|sliding|state|stream|to|tumbling|update|use|when|where|window|with)\b/,boolean:/\b(?:false|null|true)\b/i,number:/\b(?:0b[01_]*|0x[0-9a-fA-F_]*|\d[\d_]*(?:\.\d[\d_]*)?(?:[Ee][+-]?[\d_]+)?)\b/,"pattern-punctuation":{pattern:/%(?=[({[])/,alias:"punctuation"},operator:/[-+*\/%~!^]=?|=[=>]?|&[&=]?|\|[|=]?|<<?=?|>>?>?=?|(?:absent|and|not|or|present|xor)\b/,punctuation:/::|[;\[\]()\{\},.:]/},t=/#\{(?:[^"{}]|\{[^{}]*\}|"(?:[^"\\\r\n]|\\(?:\r\n|[\s\S]))*")*\}/.source,e.languages.tremor["interpolated-string"]={pattern:RegExp(/(^|[^\\])/.source+'(?:"""(?:'+/[^"\\#]|\\[\s\S]|"(?!"")|#(?!\{)/.source+"|"+t+')*"""|"(?:'+/[^"\\\r\n#]|\\(?:\r\n|[\s\S])|#(?!\{)/.source+"|"+t+')*")'),lookbehind:!0,greedy:!0,inside:{interpolation:{pattern:RegExp(t),inside:{punctuation:/^#\{|\}$/,expression:{pattern:/[\s\S]+/,inside:e.languages.tremor}}},string:/[\s\S]+/}},e.languages.troy=e.languages.tremor,e.languages.trickle=e.languages.tremor}e.exports=tremor,tremor.displayName="tremor",tremor.aliases=[]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);