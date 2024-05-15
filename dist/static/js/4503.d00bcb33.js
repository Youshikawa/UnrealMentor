"use strict";(self["webpackChunkunrealmentor"]=self["webpackChunkunrealmentor"]||[]).push([[4503],{4503:function(t,e,n){n.r(e),n.d(e,{textile:function(){return f}});n(4114);var i={addition:"inserted",attributes:"propertyName",bold:"strong",cite:"keyword",code:"monospace",definitionList:"list",deletion:"deleted",div:"punctuation",em:"emphasis",footnote:"variable",footCite:"qualifier",header:"heading",html:"comment",image:"atom",italic:"emphasis",link:"link",linkDefinition:"link",list1:"list",list2:"list.special",list3:"list",notextile:"string.special",pre:"operator",p:"content",quote:"bracket",span:"quote",specialChar:"character",strong:"strong",sub:"content.special",sup:"content.special",table:"variableName.special",tableHeading:"operator"};function a(t,e){e.mode=m.newLayout,e.tableHeading=!1,"definitionList"===e.layoutType&&e.spanningLayout&&t.match(d("definitionListEnd"),!1)&&(e.spanningLayout=!1)}function r(t,e,n){if("_"===n)return t.eat("_")?l(t,e,"italic",/__/,2):l(t,e,"em",/_/,1);if("*"===n)return t.eat("*")?l(t,e,"bold",/\*\*/,2):l(t,e,"strong",/\*/,1);if("["===n)return t.match(/\d+\]/)&&(e.footCite=!0),o(e);if("("===n){var a=t.match(/^(r|tm|c)\)/);if(a)return i.specialChar}if("<"===n&&t.match(/(\w+)[^>]+>[^<]+<\/\1>/))return i.html;if("?"===n&&t.eat("?"))return l(t,e,"cite",/\?\?/,2);if("="===n&&t.eat("="))return l(t,e,"notextile",/==/,2);if("-"===n&&!t.eat("-"))return l(t,e,"deletion",/-/,1);if("+"===n)return l(t,e,"addition",/\+/,1);if("~"===n)return l(t,e,"sub",/~/,1);if("^"===n)return l(t,e,"sup",/\^/,1);if("%"===n)return l(t,e,"span",/%/,1);if("@"===n)return l(t,e,"code",/@/,1);if("!"===n){var r=l(t,e,"image",/(?:\([^\)]+\))?!/,1);return t.match(/^:\S+/),r}return o(e)}function l(t,e,n,i,a){var r=t.pos>a?t.string.charAt(t.pos-a-1):null,l=t.peek();if(e[n]){if((!l||/\W/.test(l))&&r&&/\S/.test(r)){var u=o(e);return e[n]=!1,u}}else(!r||/\W/.test(r))&&l&&/\S/.test(l)&&t.match(new RegExp("^.*\\S"+i.source+"(?:\\W|$)"),!1)&&(e[n]=!0,e.mode=m.attributes);return o(e)}function o(t){var e=u(t);if(e)return e;var n=[];return t.layoutType&&n.push(i[t.layoutType]),n=n.concat(s(t,"addition","bold","cite","code","deletion","em","footCite","image","italic","link","span","strong","sub","sup","table","tableHeading")),"header"===t.layoutType&&n.push(i.header+"-"+t.header),n.length?n.join(" "):null}function u(t){var e=t.layoutType;switch(e){case"notextile":case"code":case"pre":return i[e];default:return t.notextile?i.notextile+(e?" "+i[e]:""):null}}function s(t){for(var e=[],n=1;n<arguments.length;++n)t[arguments[n]]&&e.push(i[arguments[n]]);return e}function c(t){var e=t.spanningLayout,n=t.layoutType;for(var i in t)t.hasOwnProperty(i)&&delete t[i];t.mode=m.newLayout,e&&(t.layoutType=n,t.spanningLayout=!0)}var p={cache:{},single:{bc:"bc",bq:"bq",definitionList:/- .*?:=+/,definitionListEnd:/.*=:\s*$/,div:"div",drawTable:/\|.*\|/,foot:/fn\d+/,header:/h[1-6]/,html:/\s*<(?:\/)?(\w+)(?:[^>]+)?>(?:[^<]+<\/\1>)?/,link:/[^"]+":\S/,linkDefinition:/\[[^\s\]]+\]\S+/,list:/(?:#+|\*+)/,notextile:"notextile",para:"p",pre:"pre",table:"table",tableCellAttributes:/[\/\\]\d+/,tableHeading:/\|_\./,tableText:/[^"_\*\[\(\?\+~\^%@|-]+/,text:/[^!"_=\*\[\(<\?\+~\^%@-]+/},attributes:{align:/(?:<>|<|>|=)/,selector:/\([^\(][^\)]+\)/,lang:/\[[^\[\]]+\]/,pad:/(?:\(+|\)+){1,2}/,css:/\{[^\}]+\}/},createRe:function(t){switch(t){case"drawTable":return p.makeRe("^",p.single.drawTable,"$");case"html":return p.makeRe("^",p.single.html,"(?:",p.single.html,")*","$");case"linkDefinition":return p.makeRe("^",p.single.linkDefinition,"$");case"listLayout":return p.makeRe("^",p.single.list,d("allAttributes"),"*\\s+");case"tableCellAttributes":return p.makeRe("^",p.choiceRe(p.single.tableCellAttributes,d("allAttributes")),"+\\.");case"type":return p.makeRe("^",d("allTypes"));case"typeLayout":return p.makeRe("^",d("allTypes"),d("allAttributes"),"*\\.\\.?","(\\s+|$)");case"attributes":return p.makeRe("^",d("allAttributes"),"+");case"allTypes":return p.choiceRe(p.single.div,p.single.foot,p.single.header,p.single.bc,p.single.bq,p.single.notextile,p.single.pre,p.single.table,p.single.para);case"allAttributes":return p.choiceRe(p.attributes.selector,p.attributes.css,p.attributes.lang,p.attributes.align,p.attributes.pad);default:return p.makeRe("^",p.single[t])}},makeRe:function(){for(var t="",e=0;e<arguments.length;++e){var n=arguments[e];t+="string"===typeof n?n:n.source}return new RegExp(t)},choiceRe:function(){for(var t=[arguments[0]],e=1;e<arguments.length;++e)t[2*e-1]="|",t[2*e]=arguments[e];return t.unshift("(?:"),t.push(")"),p.makeRe.apply(null,t)}};function d(t){return p.cache[t]||(p.cache[t]=p.createRe(t))}var m={newLayout:function(t,e){return t.match(d("typeLayout"),!1)?(e.spanningLayout=!1,(e.mode=m.blockType)(t,e)):(u(e)||(t.match(d("listLayout"),!1)?n=m.list:t.match(d("drawTable"),!1)?n=m.table:t.match(d("linkDefinition"),!1)?n=m.linkDefinition:t.match(d("definitionList"))?n=m.definitionList:t.match(d("html"),!1)&&(n=m.html)),(e.mode=n||m.text)(t,e));var n},blockType:function(t,e){var n,i;return e.layoutType=null,(n=t.match(d("type")))?(i=n[0],(n=i.match(d("header")))?(e.layoutType="header",e.header=parseInt(n[0][1])):i.match(d("bq"))?e.layoutType="quote":i.match(d("bc"))?e.layoutType="code":i.match(d("foot"))?e.layoutType="footnote":i.match(d("notextile"))?e.layoutType="notextile":i.match(d("pre"))?e.layoutType="pre":i.match(d("div"))?e.layoutType="div":i.match(d("table"))&&(e.layoutType="table"),e.mode=m.attributes,o(e)):(e.mode=m.text)(t,e)},text:function(t,e){if(t.match(d("text")))return o(e);var n=t.next();return'"'===n?(e.mode=m.link)(t,e):r(t,e,n)},attributes:function(t,e){return e.mode=m.layoutLength,t.match(d("attributes"))?i.attributes:o(e)},layoutLength:function(t,e){return t.eat(".")&&t.eat(".")&&(e.spanningLayout=!0),e.mode=m.text,o(e)},list:function(t,e){var n=t.match(d("list"));e.listDepth=n[0].length;var i=(e.listDepth-1)%3;return e.layoutType=i?1===i?"list2":"list3":"list1",e.mode=m.attributes,o(e)},link:function(t,e){return e.mode=m.text,t.match(d("link"))?(t.match(/\S+/),i.link):o(e)},linkDefinition:function(t){return t.skipToEnd(),i.linkDefinition},definitionList:function(t,e){return t.match(d("definitionList")),e.layoutType="definitionList",t.match(/\s*$/)?e.spanningLayout=!0:e.mode=m.attributes,o(e)},html:function(t){return t.skipToEnd(),i.html},table:function(t,e){return e.layoutType="table",(e.mode=m.tableCell)(t,e)},tableCell:function(t,e){return t.match(d("tableHeading"))?e.tableHeading=!0:t.eat("|"),e.mode=m.tableCellAttributes,o(e)},tableCellAttributes:function(t,e){return e.mode=m.tableText,t.match(d("tableCellAttributes"))?i.attributes:o(e)},tableText:function(t,e){return t.match(d("tableText"))?o(e):"|"===t.peek()?(e.mode=m.tableCell,o(e)):r(t,e,t.next())}};const f={name:"textile",startState:function(){return{mode:m.newLayout}},token:function(t,e){return t.sol()&&a(t,e),e.mode(t,e)},blankLine:c}}}]);
//# sourceMappingURL=4503.d00bcb33.js.map