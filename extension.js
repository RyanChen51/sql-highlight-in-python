// 这是一个空的扩展文件
// 由于我们的扩展主要是通过语法高亮规则工作，不需要额外的激活代码

// @ts-check
'use strict';

/**
 * @param {Object} context - 扩展上下文
 */
function activate(context) {
    // 这个扩展不需要任何激活代码
    console.log('Python SQL Highlighter 扩展已激活');
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
