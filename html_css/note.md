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

---

# CSS

## Introduction to CSS

### What is CSS?

- Cascading Style Sheets - language to style and lay out web pages
- Can use to style font, color, spacing, layout of page, animations
- Language for styling your document and determining how it is presented

### How can we alter the appearance of HTML with CSS?

- Web browser looks for CSS rules
- What's a CSS rule?

    - **Selector** - essentially 'selects' the HTML element(s) you want to style
    - **Properties** - properties which you want to change

### CSS Declarations

where you set the CSS properties to specific values

```CSS
some-element {
    #property: declaration;
    background-color: rgb(0, 0, 255);
    font-size: 50px;
}
```

### The Box Model (Padding, Margin and Borders)

- Each element in an HTML document can be thought of as a rectangular box
- The standard box model describes the space an element takes up
- Each box has four edges: margin, border, padding, content edges

```markdown
Margin edge
|-------------------------------------------|
|   Border edge                             |
|   |-------------------------------|       |
|   |    padding edge               |       |
|   |    |---------------------|    |       |
|   |    |    Content edge     |    |       |
|   |    |    |------------|   |    |       |
|   |    |    |            |   |    |       |
|   |    |    |------------|   |    |       |
|   |    |---------------------|    |       |
|   |-------------------------------|       |
|-------------------------------------------|
```

### Background Color and Font Size

```CSS
body {
    background-color: forestgreen;
}

section {
    background-color: orange;
}

p {
    font-size: 25px;
}
```

## Intermediate CSS

### Width and Text Alignment

```CSS
/* add padding and margin */
p {
    padding-left: 10px;
    /* etc. */
    margin-top: 10px;
}

/* add text alignment and width
If change properties of parent,
all children inherit that propertis.
That's what cascade means */
main {
    width: 1000px;
}

h1 {
    text-align: center;
}
```

### Inheritance (Cascading)

```CSS
main {
    width: 1000px;
    color: blue;
}

/* Width gonna be 1000px */
section {
    width: inherit;
}

/* The color of 'p' will be blue */
p {
    color: inherit;
}

/* The color of 'h1' will be h1 */
h1 {
    color: orange;
}
```

### Type Selectors

```CSS
/* parent parent child ... */
main section ul {
    background-color: green;
}
```

### Direct Descendants

\<example html>

```HTML
<!-- ... -->
<body>
    <section>
        <div>
            <h4>This is h4</h4>
            <div>
                <h4>The innermost h4</h4>
            </div>
        </div>
    </section>
</body>
```

```CSS
/* This changes color of the outmost h4 in div */
section > div > h4 {
    color: yellow;
}
```

### Classes

```CSS
.example-div {
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: limegreen;
}

.cursive {
    font-family: cursive;
}

/* you can use class with direct descendant */
section > .example-div {
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: limegreen;
}

/* or like this */
.example-div .cursive-h4 {
    font-family: cursive;
}
```

```HTML
<!-- use class like this -->
<div class="example-div">
    <p> hello! </p>
</div>

<section>
    <!-- you can apply different classes at once -->
    <div class="example-div cursive">
        <p>This is p in section > example-div</p>
    </div>
</section>
```

### IDs

ID should be unique in page.

```HTML
<section id="id1">
    <h4>This is h4 in id1</h4>
</section>
```

```CSS
/* use hashtag to select id */
#id1 > h4 {
    color: skyblue;
    font-family: cursive;
}

/* or */
section#id1 {
    color: orange;
}
```

## Advanced CSS

### Specificity

- Specificity is super important with CSS.  

    0. Type selectors (e.g. h1, div, header, p)
    1. Class selectors (e.g. .example-class)
    2. ID selectors (e.g. #example)

classes are more specific than descendant selector.
ID is the most specific selector.

### Advanced Selectors

```CSS
/* select p and h3 in example. comma is important*/
#example p, h3 {
    color: yellow;
}

/* psuedo class */
#example p:first-child {
    color: red;
}

#example p:last-child {
    color: red;
}

#example p:hover {
    filter: invert(100);
    transform: scale(2);
}
/* select sibling element. select p directly next to h3*/
#example h3+p {
    color: red;
}

#example h3 + p {
    color: red;
}
```

## CSS Responsiveness

```CSS
/* display mode */
nav ul {
    display: flex;
    justify-content: space-around;
}

nav ul li {
    /* clock-wise top > right > bottom > left */
    margin: 0 10px 0 10px;
    /* If there are two values, first one is top-bottom and the last one is left-right padding */
    padding: 10px 10px;
}

/* border */
ul {
    border-radius: 10px;
}

/* responsiveness */
img {
    width: 25%;
    height: auto;
}

main {
    display: flex;
    flex-flow: row wrap-reverse;
    justify-content: center;
}
```
