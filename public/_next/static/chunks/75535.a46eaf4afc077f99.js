(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[75535,68],{75535:function(e,t,n){"use strict";var o=n(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var a=o(n(64262)).default;t.default=a},64262:function(e){"use strict";function moonscript(e){e.languages.moonscript={comment:/--.*/,string:[{pattern:/'[^']*'|\[(=*)\[[\s\S]*?\]\1\]/,greedy:!0},{pattern:/"[^"]*"/,greedy:!0,inside:{interpolation:{pattern:/#\{[^{}]*\}/,inside:{moonscript:{pattern:/(^#\{)[\s\S]+(?=\})/,lookbehind:!0,inside:null},"interpolation-punctuation":{pattern:/#\{|\}/,alias:"punctuation"}}}}}],"class-name":[{pattern:/(\b(?:class|extends)[ \t]+)\w+/,lookbehind:!0},/\b[A-Z]\w*/],keyword:/\b(?:class|continue|do|else|elseif|export|extends|for|from|if|import|in|local|nil|return|self|super|switch|then|unless|using|when|while|with)\b/,variable:/@@?\w*/,property:{pattern:/\b(?!\d)\w+(?=:)|(:)(?!\d)\w+/,lookbehind:!0},function:{pattern:/\b(?:_G|_VERSION|assert|collectgarbage|coroutine\.(?:create|resume|running|status|wrap|yield)|debug\.(?:debug|getfenv|gethook|getinfo|getlocal|getmetatable|getregistry|getupvalue|setfenv|sethook|setlocal|setmetatable|setupvalue|traceback)|dofile|error|getfenv|getmetatable|io\.(?:close|flush|input|lines|open|output|popen|read|stderr|stdin|stdout|tmpfile|type|write)|ipairs|load|loadfile|loadstring|math\.(?:abs|acos|asin|atan|atan2|ceil|cos|cosh|deg|exp|floor|fmod|frexp|ldexp|log|log10|max|min|modf|pi|pow|rad|random|randomseed|sin|sinh|sqrt|tan|tanh)|module|next|os\.(?:clock|date|difftime|execute|exit|getenv|remove|rename|setlocale|time|tmpname)|package\.(?:cpath|loaded|loadlib|path|preload|seeall)|pairs|pcall|print|rawequal|rawget|rawset|require|select|setfenv|setmetatable|string\.(?:byte|char|dump|find|format|gmatch|gsub|len|lower|match|rep|reverse|sub|upper)|table\.(?:concat|insert|maxn|remove|sort)|tonumber|tostring|type|unpack|xpcall)\b/,inside:{punctuation:/\./}},boolean:/\b(?:false|true)\b/,number:/(?:\B\.\d+|\b\d+\.\d+|\b\d+(?=[eE]))(?:[eE][-+]?\d+)?\b|\b(?:0x[a-fA-F\d]+|\d+)(?:U?LL)?\b/,operator:/\.{3}|[-=]>|~=|(?:[-+*/%<>!=]|\.\.)=?|[:#^]|\b(?:and|or)\b=?|\b(?:not)\b/,punctuation:/[.,()[\]{}\\]/},e.languages.moonscript.string[1].inside.interpolation.inside.moonscript.inside=e.languages.moonscript,e.languages.moon=e.languages.moonscript}e.exports=moonscript,moonscript.displayName="moonscript",moonscript.aliases=["moon"]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);