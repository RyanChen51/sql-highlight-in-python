# Python SQL Highlighter

This VS Code extension highlights SQL code in Python files, making your code more readable and maintainable.

## Features

- **Auto Detection**: Intelligently recognizes SQL code in Python multiline strings without any special markers
- Supports common SQL syntax highlighting

## Installation

Search for "Python SQL Highlighter" in the extension marketplace and install it

## Usage

### Auto Detection Mode (Recommended)

The extension automatically detects SQL code in Python multiline strings (triple-quoted strings) and applies highlighting. Detection is based on the following rules:

1. String contains common SQL keywords (such as SELECT, INSERT, UPDATE, CREATE, etc.)
2. String contains SQL syntax structures (such as FROM, WHERE, JOIN, etc.)
3. Variable name contains "sql" or "query"

### Explicit Marking Mode (Optional)

You can still use explicit markers to ensure specific code is recognized as SQL. Add `--sql` marker at the beginning of the Python multiline string, and a semicolon `;`, `--endsql` or `--end-sql` marker at the end.

Example:

```python
sql_query = """
--sql
SELECT *
FROM users
WHERE age > 18
ORDER BY name;
--endsql
"""
```

## License

This extension is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Made by Darran Zhang from [codelast.com](https://codelast.com)

<br><br><br><br><br>

# Python SQL 高亮插件

这个VS Code扩展可以高亮显示Python文件中的SQL代码，使代码更易读和维护。

## 功能

- **自动检测**：智能识别Python多行字符串中的SQL代码，无需添加特殊标记
- 支持常见的SQL语法高亮

## 安装

在扩展市场中搜索"Python SQL Highlighter"并安装

## 使用方法

### 自动检测模式（推荐）

插件会自动检测Python多行字符串（三引号字符串）中的SQL代码并应用高亮。检测基于以下规则：

1. 字符串包含常见SQL关键词（如SELECT, INSERT, UPDATE, CREATE等）
2. 字符串包含SQL语法结构（如FROM, WHERE, JOIN等）
3. 变量名包含"sql"或"query"

### 显式标记模式（可选）

您仍然可以使用显式标记来确保特定代码被识别为SQL。在Python多行字符串的开头添加 `--sql` 标记，在结尾处添加分号 `;`、`--endsql` 或 `--end-sql` 标记。

示例：

```python
sql_query = """
--sql
SELECT *
FROM users
WHERE age > 18
ORDER BY name;
--endsql
"""
```
## 许可证

本扩展基于 MIT 许可证发布。详情请查看 [LICENSE](LICENSE) 文件。

---
作者：Darran Zhang @ [codelast.com](https://codelast.com)
