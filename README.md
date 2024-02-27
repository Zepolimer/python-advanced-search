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


## Use cases
You can use search method with common operators and specific for each search-engine.  
Your query can be combined with exclude method to add a minus in front of an operator or expression.  
You can use OR, AND, NOT classes which allows you to perform conditional query.

<br/>

#### Google (many params available on search and exclude methods)

```python
from python_advanced_search.engines.google.query import GoogleQuery

query = GoogleQuery().include(
    indexed='domain.tld',
    all_in_anchor='anchor',
).exclude(
    in_anchor='scholar'
)

# return query string
# query.str = 'site:domain.tld allinanchor:anchor -inanchor:scholar'
```

#### Bing (many params available on search and exclude methods)

```python
from python_advanced_search.engines.bing.query import BingQuery

query = BingQuery().include(
    indexed='domain.tld',
    in_body='text_content',
)

# return query string
# query.str = 'site:domain.tld inbody:text_content'
```


#### Conditional (available for GoogleQuery and BingQuery)

```python
from python_advanced_search.engines.bing.query import BingQuery
from python_advanced_search.models.commands.conditions import AND

query = BingQuery().include(
    indexed='domain.tld',
    in_body=AND('text_content_1', 'text_content_2'),
)

# return query string
# query.str = 'site:domain.tld inbody:(text_content_1 AND text_content_2)'
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

