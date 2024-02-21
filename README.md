# python-advanced-search
<br/>

Search-engine advanced queries for Google and Bing  


## Installation
```commandline
pip install git+ssh://git@github.com/Zepolimer/python-advanced-search.git@main#python-advanced-search
```

```commandline
python3 -m unittest
```

```commandline
rm build/ python_advanced_search.egg-info dist -Rf
python3 setup.py bdist_wheel
pip3 install -I dist/python_advanced_search-*-py3-none-any.whl
```
<br/>

### Operators
| Command                      | Google                     | Bing               | Common |
|------------------------------|----------------------------|--------------------|--------|
| exact search                 | `""`                       | `""`               | ✅      |
| indexed (domain)             | `site:`                    | `site:`            | ✅      |
| indexed (URL)                | `site:`                    | `url:`             | ✅      |
| page title                   | `allintitle:` `intitle:`   | `intitle:`         | ✅      |
| page body                    | `allintext:` `intext:`     | `inbody:`          | ✅      |
| page url                     | `allinurl:` `inurl:`       | N/A                | ❌      |
| page anchor                  | `allinanchor:` `inanchor:` | N/A                | ❌      |
| include (word or operator)   | `AND`                      | `AND`              | ✅      |
| comparison (a OR b)          | `OR`                       | `OR`               | ✅      |
| exclude (word or operator)   | `-`                        | `-`                | ✅      |
| exclude (word or expression) | `NOT`                      | `NOT`              | ✅      |
| between                      | `..`                       | N/A                | ❌      |
| restricted location          | N/A                        | `location:` `loc:` | ❌      |
| restricted language          | N/A                        | `language:`        | ❌      |
| restricted filetype          | `filetype:`                | `filetype:`        | ✅      |
| similar content (URL)        | `related:`                 | N/A                | ❌      |
| define word                  | `define:`                  | N/A                | ❌      |
| link from domain             | N/A                        | `linkfromdomain:`  | ❌      |
| link domain                  | N/A                        | `linkdomain:`      | ❌      |

