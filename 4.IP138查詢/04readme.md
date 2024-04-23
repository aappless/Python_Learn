text()獲取當前結點下的子文本結點.(不是獲取後裔結點的文本結點)

> 注意,text()不是函數，是文本結點，文本結點從屬於其父結點，所以`./text()`只能獲取位於其子節點位置的文本結點，不會獲取位於其後裔結點位置的文本結點,想要獲取一個標籤下的所有文本數據，就需要用`.//text()`

string(\$arg) : [DOC](https://www.w3.org/TR/xpath-functions-31/#func-string) 獲取當前結點下的所有文本內容的字符串.具體用法在DOC中有,\$args其中一種值是xpath表達式，函數返回xpath表達式所選結點下面的所有文本內容組成的字符串，就像是在瀏覽器中看到的那樣.

簡單記憶就是text()獲取的是一個字符串列表,string()獲取的是字符串.

----------------------------

XPath中text方法和string方法

text()方法**

text()又有兩種用法，一種是ls[1].xpath('./text()')，一種是ls[1].xpath('.//text()')。

ls[1].xpath('./text()')用法

表示只取當前節點中的文本內容，對於子孫節點的內容不會取。

##### ls[1].xpath('.//text()')用法

表示取當前節點及其子孫節點中的文本內容。

**string()方法**

string()會把當前節點和所有的子孫節點中的文本全部提取出來，組合成一個字符串。


https://cloud.tencent.com/developer/article/1447667

https://zhuanlan.zhihu.com/p/29436838
