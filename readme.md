
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
        <td><html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=utf-8">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List href="clang_html.fld/filelist.xml">
<!--[if gte mso 9]><xml>
 <o:DocumentProperties>
  <o:Author>Microsoft Office User</o:Author>
  <o:LastAuthor>Microsoft Office User</o:LastAuthor>
  <o:Revision>2</o:Revision>
  <o:TotalTime>0</o:TotalTime>
  <o:LastPrinted>2021-02-11T18:33:00Z</o:LastPrinted>
  <o:Created>2021-02-11T18:52:00Z</o:Created>
  <o:LastSaved>2021-02-11T18:52:00Z</o:LastSaved>
  <o:Pages>1</o:Pages>
  <o:Words>559</o:Words>
  <o:Characters>3189</o:Characters>
  <o:Lines>26</o:Lines>
  <o:Paragraphs>7</o:Paragraphs>
  <o:CharactersWithSpaces>3741</o:CharactersWithSpaces>
  <o:Version>16.00</o:Version>
 </o:DocumentProperties>
 <o:OfficeDocumentSettings>
  <o:AllowPNG/>
 </o:OfficeDocumentSettings>
</xml><![endif]-->
<link rel=themeData href="clang_html.fld/themedata.thmx">
<link rel=colorSchemeMapping href="clang_html.fld/colorschememapping.xml">
<!--[if gte mso 9]><xml>
 <w:WordDocument>
  <w:SpellingState>Clean</w:SpellingState>
  <w:GrammarState>Clean</w:GrammarState>
  <w:TrackMoves>false</w:TrackMoves>
  <w:TrackFormatting/>
  <w:PunctuationKerning/>
  <w:ValidateAgainstSchemas/>
  <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
  <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
  <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
  <w:DoNotPromoteQF/>
  <w:LidThemeOther>EN-GB</w:LidThemeOther>
  <w:LidThemeAsian>X-NONE</w:LidThemeAsian>
  <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
  <w:Compatibility>
   <w:BreakWrappedTables/>
   <w:SnapToGridInCell/>
   <w:WrapTextWithPunct/>
   <w:UseAsianBreakRules/>
   <w:DontGrowAutofit/>
   <w:SplitPgBreakAndParaMark/>
   <w:EnableOpenTypeKerning/>
   <w:DontFlipMirrorIndents/>
   <w:OverrideTableStyleHps/>
  </w:Compatibility>
  <m:mathPr>
   <m:mathFont m:val="Cambria Math"/>
   <m:brkBin m:val="before"/>
   <m:brkBinSub m:val="&#45;-"/>
   <m:smallFrac m:val="off"/>
   <m:dispDef/>
   <m:lMargin m:val="0"/>
   <m:rMargin m:val="0"/>
   <m:defJc m:val="centerGroup"/>
   <m:wrapIndent m:val="1440"/>
   <m:intLim m:val="subSup"/>
   <m:naryLim m:val="undOvr"/>
  </m:mathPr></w:WordDocument>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
  DefSemiHidden="false" DefQFormat="false" DefPriority="99"
  LatentStyleCount="376">
  <w:LsdException Locked="false" Priority="0" QFormat="true" Name="Normal"/>
  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 1"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 2"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 3"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 4"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 5"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 6"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 7"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 8"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 9"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 1"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 2"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 3"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 4"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 5"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 6"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 7"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 8"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="header"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footer"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index heading"/>
  <w:LsdException Locked="false" Priority="35" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="caption"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of figures"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope return"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="line number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="page number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of authorities"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="macro"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="toa heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 5"/>
  <w:LsdException Locked="false" Priority="10" QFormat="true" Name="Title"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Closing"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Signature"/>
  <w:LsdException Locked="false" Priority="1" SemiHidden="true"
   UnhideWhenUsed="true" Name="Default Paragraph Font"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Message Header"/>
  <w:LsdException Locked="false" Priority="11" QFormat="true" Name="Subtitle"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Salutation"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Date"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Note Heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Block Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="FollowedHyperlink"/>
  <w:LsdException Locked="false" Priority="22" QFormat="true" Name="Strong"/>
  <w:LsdException Locked="false" Priority="20" QFormat="true" Name="Emphasis"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Document Map"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Plain Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="E-mail Signature"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Top of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Bottom of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal (Web)"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Acronym"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Cite"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Code"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Definition"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Keyboard"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Preformatted"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Sample"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Typewriter"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Variable"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Table"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation subject"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="No List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Contemporary"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Elegant"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Professional"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Balloon Text"/>
  <w:LsdException Locked="false" Priority="39" Name="Table Grid"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Theme"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Placeholder Text"/>
  <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Revision"/>
  <w:LsdException Locked="false" Priority="34" QFormat="true"
   Name="List Paragraph"/>
  <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
  <w:LsdException Locked="false" Priority="30" QFormat="true"
   Name="Intense Quote"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="19" QFormat="true"
   Name="Subtle Emphasis"/>
  <w:LsdException Locked="false" Priority="21" QFormat="true"
   Name="Intense Emphasis"/>
  <w:LsdException Locked="false" Priority="31" QFormat="true"
   Name="Subtle Reference"/>
  <w:LsdException Locked="false" Priority="32" QFormat="true"
   Name="Intense Reference"/>
  <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
  <w:LsdException Locked="false" Priority="37" SemiHidden="true"
   UnhideWhenUsed="true" Name="Bibliography"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
  <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
  <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
  <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
  <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
  <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
  <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
  <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Mention"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Smart Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hashtag"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Unresolved Mention"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Smart Link"/>
 </w:LatentStyles>
</xml><![endif]-->
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:variable;
	mso-font-signature:-536870145 1107305727 0 0 415 0;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-536859905 -1073732485 9 0 511 0;}
@font-face
	{font-family:Menlo;
	panose-1:2 11 6 9 3 8 4 2 2 4;
	mso-font-alt:Menlo;
	mso-font-charset:0;
	mso-generic-font-family:modern;
	mso-font-pitch:fixed;
	mso-font-signature:-436198657 -771687941 33554472 0 479 0;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-parent:"";
	margin:0cm;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:Calibri;
	mso-fareast-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-fareast-language:EN-US;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
	{mso-style-priority:99;
	mso-style-link:"Header Char";
	margin:0cm;
	mso-pagination:widow-orphan;
	tab-stops:center 225.65pt right 451.3pt;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:Calibri;
	mso-fareast-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-fareast-language:EN-US;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
	{mso-style-priority:99;
	mso-style-link:"Footer Char";
	margin:0cm;
	mso-pagination:widow-orphan;
	tab-stops:center 225.65pt right 451.3pt;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:Calibri;
	mso-fareast-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-fareast-language:EN-US;}
span.HeaderChar
	{mso-style-name:"Header Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:Header;}
span.FooterChar
	{mso-style-name:"Footer Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:Footer;}
span.SpellE
	{mso-style-name:"";
	mso-spl-e:yes;}
span.GramE
	{mso-style-name:"";
	mso-gram-e:yes;}
.MsoChpDefault
	{mso-style-type:export-only;
	mso-default-props:yes;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:Calibri;
	mso-fareast-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-fareast-language:EN-US;}
 /* Page Definitions */
 @page
	{mso-footnote-separator:url("clang_html.fld/header.html") fs;
	mso-footnote-continuation-separator:url("clang_html.fld/header.html") fcs;
	mso-endnote-separator:url("clang_html.fld/header.html") es;
	mso-endnote-continuation-separator:url("clang_html.fld/header.html") ecs;}
@page WordSection1
	{size:1191.0pt 842.0pt;
	mso-page-orientation:landscape;
	margin:72.0pt 72.0pt 72.0pt 72.0pt;
	mso-header-margin:35.4pt;
	mso-footer-margin:35.4pt;
	mso-paper-source:0;}
div.WordSection1
	{page:WordSection1;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:"Table Normal";
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-priority:99;
	mso-style-parent:"";
	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
	mso-para-margin:0cm;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-fareast-language:EN-US;}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext="edit" spidmax="1026"/>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext="edit">
  <o:idmap v:ext="edit" data="1"/>
 </o:shapelayout></xml><![endif]-->
</head>

<body lang=EN-GB style='tab-interval:36.0pt;word-wrap:break-word'>

<div class=WordSection1>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'>$ clang -<span class=SpellE>Xclang</span> -<span class=SpellE>ast</span>-dump
<span class=SpellE>some_file.c</span><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>TranslationUnitDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042008</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid <span
class=SpellE>sloc</span>&gt;</span><span style='font-size:11.0pt;font-family:
Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;font-family:
Menlo;color:#9FA01C'>&lt;invalid <span class=SpellE>sloc</span>&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>TypedefDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910428c0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid <span
class=SpellE>sloc</span>&gt;</span><span style='font-size:11.0pt;font-family:
Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;font-family:
Menlo;color:#9FA01C'>&lt;invalid <span class=SpellE>sloc</span>&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __int128_t</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'__int128'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>BuiltinType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910425a0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'__int128'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>TypedefDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042930</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid <span
class=SpellE>sloc</span>&gt;</span><span style='font-size:11.0pt;font-family:
Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;font-family:
Menlo;color:#9FA01C'>&lt;invalid <span class=SpellE>sloc</span>&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __uint128_t</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'unsigned __int128'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>BuiltinType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910425c0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'unsigned __int128'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>TypedefDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042c38</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid <span
class=SpellE>sloc</span>&gt;</span><span style='font-size:11.0pt;font-family:
Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;font-family:
Menlo;color:#9FA01C'>&lt;invalid <span class=SpellE>sloc</span>&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __<span class=SpellE>NSConstantString</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __<span
class=SpellE>NSConstantString_tag</span>'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>RecordType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042a10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __<span
class=SpellE>NSConstantString_tag</span>'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>`-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Record</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042988</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> '__<span
class=SpellE>NSConstantString_tag</span>'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>TypedefDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042cd0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid <span
class=SpellE>sloc</span>&gt;</span><span style='font-size:11.0pt;font-family:
Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;font-family:
Menlo;color:#9FA01C'>&lt;invalid <span class=SpellE>sloc</span>&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __<span class=SpellE>builtin_ms_va_list</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'char *'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>PointerType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042c90</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'char *'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>BuiltinType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910420a0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'char'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>TypedefDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fa00</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>&lt;invalid <span
class=SpellE>sloc</span>&gt;</span><span style='font-size:11.0pt;font-family:
Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;font-family:
Menlo;color:#9FA01C'>&lt;invalid <span class=SpellE>sloc</span>&gt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> implicit</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> __<span class=SpellE>builtin_va_list</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __<span
class=SpellE>va_list_tag</span> [1]'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>ConstantArrayType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042f70</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __<span
class=SpellE>va_list_tag</span> [1]'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'> 1 <o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>RecordType</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042db0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'struct __<span
class=SpellE>va_list_tag</span>'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>     </span>`-</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Record</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591042d28</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> '__<span
class=SpellE>va_list_tag</span>'</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107faa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>some_file.c:1:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> <span class=SpellE>baz</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fbb0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:3:1</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:14</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> foo</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC6AF8'>CompoundStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fc50</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:14</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fc80</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:5:1</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:8:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:5:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> bar</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC6AF8'>CompoundStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fdf8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:8:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>|-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fd80</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:6:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>| `-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fd68</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>|<span
style='mso-spacerun:yes'>   </span>`-</span><span class=SpellE><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
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
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fdd8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:7:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>     </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fdc0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>       </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fda0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107faa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> '<span class=SpellE>baz</span>'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fe38</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> <span class=SpellE>prev</span>
0x7fc59107faa8 &lt;</span><span class=GramE><span style='font-size:11.0pt;
font-family:Menlo;color:#9FA01C'>line:10:1</span></span><span style='font-size:
11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span style='font-size:11.0pt;
font-family:Menlo;color:#9FA01C'>line:13:1</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'>&gt; </span><span style='font-size:11.0pt;
font-family:Menlo;color:#9FA01C'>line:10:6</span><span style='font-size:11.0pt;
font-family:Menlo;color:#F2F2F2'> used</span><span style='font-size:11.0pt;
font-family:Menlo;color:#2EAEBB'> <span class=SpellE>baz</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC6AF8'>CompoundStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff70</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:13:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>IfStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff50</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:11:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:12:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>     </span>|-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>IntegerLiteral</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fed8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:11:9</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'int'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>     </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff30</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:12:9</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>       </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ff18</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>         </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
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
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ffa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:15:1</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:15</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> <span class=SpellE>bizz</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC6AF8'>CompoundStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080048</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:15</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080078</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:17:1</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:19:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:17:6</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> used</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> buzz</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>| `-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC6AF8'>CompoundStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080170</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:13</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:19:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>   </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080150</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:18:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>     </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080138</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>|<span style='mso-spacerun:yes'>       </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080118</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107ffa8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> '<span class=SpellE>bizz</span>'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'>`-</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#2FB41D'>FunctionDecl</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910801e0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:21:1</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:25:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:21:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> main</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'int ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>  </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CompoundStmt</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080388</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:12</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:25:1</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>|-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802b8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:22:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>| `-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802a0</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>|<span
style='mso-spacerun:yes'>   </span>`-</span><span class=SpellE><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
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
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>|-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080310</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:23:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:9</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>| `-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802f8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>|<span
style='mso-spacerun:yes'>   </span>`-</span><span class=SpellE><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc5910802d8</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc59107fe38</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> '<span class=SpellE>baz</span>'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>    </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>CallExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080368</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
class=GramE><span style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>line:24:5</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>, </span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:10</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'><o:p></o:p></span></p>

<p class=MsoNormal style='tab-stops:28.0pt 56.0pt 84.0pt 112.0pt 140.0pt 168.0pt 196.0pt 224.0pt 252.0pt 280.0pt 308.0pt 336.0pt;
background:black;mso-background-themecolor:text1;mso-layout-grid-align:none;
text-autospace:none'><span style='font-size:11.0pt;font-family:Menlo;
color:#A2AFAB'><span style='mso-spacerun:yes'>      </span>`-</span><span
class=SpellE><span style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>ImplicitCastExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080350</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void (<span
class=GramE>*)(</span>)'</span><span style='font-size:11.0pt;font-family:Menlo;
color:#F2F2F2'> &lt;</span><span class=SpellE><span style='font-size:11.0pt;
font-family:Menlo;color:#FC2218'>FunctionToPointerDecay</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt;<o:p></o:p></span></p>

<p class=MsoNormal style='background:black;mso-background-themecolor:text1'><span
style='font-size:11.0pt;font-family:Menlo;color:#A2AFAB'><span
style='mso-spacerun:yes'>        </span>`-</span><span class=SpellE><span
style='font-size:11.0pt;font-family:Menlo;color:#FC6AF8'>DeclRefExpr</span></span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080330</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> &lt;</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'>col:5</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'>&gt; </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>Function</span><span
style='font-size:11.0pt;font-family:Menlo;color:#9FA01C'> 0x7fc591080078</span><span
style='font-size:11.0pt;font-family:Menlo;color:#2EAEBB'> 'buzz'</span><span
style='font-size:11.0pt;font-family:Menlo;color:#F2F2F2'> </span><span
style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'>'void ()'<o:p></o:p></span></p>

<p class=MsoNormal><span style='font-size:11.0pt;font-family:Menlo;color:#2FB41D'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal><o:p>&nbsp;</o:p></p>

</div>

</body>

</html>
</td>
    </tr>
</table>





