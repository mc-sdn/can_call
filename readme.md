
# `can_call`

[![HitCount](http://hits.dwyl.com/mc-sdn/can_call.svg)](http://hits.dwyl.com/mc-sdn/can_call)



## About the `can_call`

`can_call` is a toy script to check if there exists a path between two vertices in the execution path of functions that a C program goes through.
`can_call` parses and analyses C code in Python with Clang which enables such usage through `libclang` (with Python bindings).


## Requirements

* LLVM/Clang -- check out the [getting
  started](http://clang.llvm.org/get_started.html) guide to find out how to obtain Clang from source. `libclang` is
  built and installed along with the Clang compiler.

----

**Please note**: Unfortunately, the state of documentation for `libclang` and its Python bindings is very lacking. 

----


## Usage

If you are running `can_call` from the terminal, just pass the arguments after the script name as follows:

```console
python3 can_call <filename> <caller> <callee>
```
where

- `<some_file.c>` is a C file
- `<caller>` is the name of a function declared in `<some_file.c>`
- `<callee>` is the name of a function declared in `<some_file.c>`

### Example


Suppose we invoke `can_call` on the C-code `some_file.c` below: 

```c
void baz(); // prototype

void foo() { }

void bar() {
    foo();
    baz();
}

void baz() {
    if (0)
        bar();
}

void bizz() { }

void buzz() {
    bizz();
}

int main() {
    foo();
    baz();
    buzz();
}
```

Executing `can_call` to find whether exists a path in the call graph for `some_file.c` from `caller`-function to `callee`-one, given in the table, we get:

| `caller`    | `callee` | Expected Output   |
| ----------- | ---------|----------|
| main        | baz      | True      |
| baz         | bar      | True      |
| buzz        | foo      | None      |
| baz         | baz      | True      |


```console
$ python3 can_call.py some_file.c main baz
True
$ python3 can_call.py some_file.c baz bar
True
$ python3 can_call.py some_file.c buzz foo
None
$ python3 can_call.py some_file.c baz baz
True
```

Clang converts the C-files into an abstract syntax tree (AST) and manipulates the AST. 
Clang has also a builtin AST-dump mode; below, the `some_file.c` converted into an AST.


<table>
    <tr>
        <td>


<html>



<body lang=EN-GB style='word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>$ clang -Xclang
-ast-dump some_file.c</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>TranslationUnitDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042008</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>TypedefDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910428c0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __int128_t</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'__int128'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>BuiltinType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910425a0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'__int128'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>TypedefDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042930</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __uint128_t</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'unsigned __int128'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>BuiltinType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910425c0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'unsigned __int128'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>TypedefDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042c38</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __NSConstantString</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct
__NSConstantString_tag'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>RecordType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042a10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct
__NSConstantString_tag'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Record</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042988</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'>
'__NSConstantString_tag'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>TypedefDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042cd0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __builtin_ms_va_list</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'char *'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>PointerType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042c90</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'char *'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>BuiltinType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910420a0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'char'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>TypedefDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fa00</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid sloc&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __builtin_va_list</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __va_list_tag
[1]'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>ConstantArrayType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042f70</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __va_list_tag
[1]'</span><span style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> 1 </span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>RecordType</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042db0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __va_list_tag'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|     `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Record</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042d28</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> '__va_list_tag'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107faa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>some_file.c:1:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> baz</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fbb0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:3:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:14</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> foo</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fc50</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:14</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fc80</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:5:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:8:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:5:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> bar</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fdf8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:8:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   |-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fd80</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:6:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   | `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fd68</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   |   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fd20</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fbb0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'foo'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fdd8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:7:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|     `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fdc0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|       `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fda0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107faa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'baz'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fe38</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> prev 0x7fc59107faa8
&lt;</span><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:10:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:13:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:10:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> baz</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff70</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:13:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>IfStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff50</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:11:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:12:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|     |-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>IntegerLiteral</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fed8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:11:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'int'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 0</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|     `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff30</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:12:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|       `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff18</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|         `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fef8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fc80</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'bar'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ffa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:15:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:15</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> bizz</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080048</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:15</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080078</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:17:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:19:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:17:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> buzz</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>| `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080170</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:19:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080150</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:18:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|     `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080138</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>|       `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080118</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ffa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'bizz'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>`-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>FunctionDecl</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910801e0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:21:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:25:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:21:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> main</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'int ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>  `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080388</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:25:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    |-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802b8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:22:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    | `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802a0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    |   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080280</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fbb0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'foo'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    |-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080310</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:23:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    | `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802f8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    |   `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802d8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fe38</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'baz'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>    `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080368</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:24:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span></p>

<p class=MsoNormal style='background:black;text-autospace:none'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'>      `-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080350</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (*)()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;</span></p>

<p class=MsoNormal style='background:black'><span style='font-size:11.0pt;
font-family:Menlo;color:#A2AFAB'>        `-</span><span style='font-size:11.0pt;
font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span><span style='font-size:11.0pt;
font-family:Menlo;color:#9FA01C'> 0x7fc591080330</span><span style='font-size:
11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span style='font-size:
11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span style='font-size:
11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:
11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span style='font-size:
11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>Function</span><span style='font-size:11.0pt;
font-family:Menlo;color:#9FA01C'> 0x7fc591080078</span><span style='font-size:
11.0pt;font-family:Menlo;color:#2EAEBB'> 'buzz'</span><span style='font-size:
11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>'void ()'</span></p>

<p class=MsoNormal><span style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>&nbsp;</span></p>

<p class=MsoNormal>&nbsp;</p>

</div>

</body>

</html>



</td>
    </tr>
</table>





