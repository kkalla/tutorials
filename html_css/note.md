# HTML Basics

## What is HTML?
- Hypertext Markup Language - standard markup language used to create web pages
- Basically tells your browser how to display web pages

## What does HTML look like?
- HTML uses tags and elements to enclose different parts of the content

<p> My name is max </p>
<p> A- </p>

E.g.:

<!DOCTYPE html> # informs the browser that the document type is html
<html>          # wraps all content
<head>          # put content here that shouldn't be shown to visitors
                # E.g.: link to style sheets or JavaScript files
    <meta charset='utf-8'>
    <title> My Title </title>
</head>
<body>          # contains all the content you want to show visitors
    <p> Hello, welcome </p>
</body>
</html>

## [JS Bin](https://jsbin.com/?html,output)
debug javascript here.

## HTML Lists
### Lists and comments
1. ordered list
```html
<!-- Ordered list -->
<ol>
    <li>one</li>
    <li>two</li>
    <li>three</li>
    <li>four</li>
</ol>
```
becomes
<ol>
    <li>one</li>
    <li>two</li>
    <li>three</li>
    <li>four</li>
</ol>

2. unordered list
```html
<!-- Unordered list -->
<ul>
    <li>first</li>
    <li>second</li>
    <li>third</li>
    <li>fourth</li>
</ul>
```
becomes
<!-- Unordered list -->
<ul>
    <li>first</li>
    <li>second</li>
    <li>third</li>
    <li>fourth</li>
</ul>

### Nested Lists

```html
<!-- Nested list -->
<ol>
    <li>one</li>
    <li>two</li>
    <ul>
        <li>A in two</li>
        <li>B in two</li>
    </ul>
    <li>three</li>
    <li>four</li>
</ol>
```
becomes
<!-- Nested list -->
<ol>
    <li>one</li>
    <li>two</li>
    <ul>
        <li>A in two</li>
        <li>B in two</li>
    </ul>
    <li>three</li>
    <li>four</li>
</ol>

## Images
```html
<img src="https://cdn.shopify.com/s/files/1/2658/1334/products/HDR2386_1024x1024.jpg?v=1571678336" alt="galaxy backdrop">
```

### Images in lists
```html
<ul>
    <li><img src="https://media.gettyimages.com/photos/milky-way-galaxy-background-picture-id1018193742?s=2048x2048"></li>
    <li><img src="https://media.gettyimages.com/photos/starry-night-picture-id519760984?s=2048x2048"></li>
</ul>
```

## HTML Links
### Links
```html
<a href="http://www.google.com">Go to Google</a>
```
becomes
<a href="http://www.google.com">Go to Google</a>

### Images as Links
```html
<a href="https://i.imgur.com/zzCYQpc.png">
    <img src="https://i.imgur.com/zzCYQpc.png"/>
</a>
```
becomes
<a href="https://i.imgur.com/zzCYQpc.png">
    <img src="https://i.imgur.com/zzCYQpc.png"/>
</a>

### Email Links
```html
<a href="mailto:myname@domain.com">Email me</a>
```

## More HTML Tags
### Div, Header, Footer and Main
```html
<!-- Start of header -->
<header>
    <p>header - p1</p>
    <p>header - p2</p>
</header>
<!-- end of header -->
<!-- start of main content -->
<main>
    <p>MAIN</p>
</main>
<!-- end of main content -->
<!-- Start of footer -->
<footer>
    <p>Footer</p>
</footer>
<!-- end of footer -->
```