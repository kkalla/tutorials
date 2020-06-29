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

## The Box Model (Padding, Margin and Borders)

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

## Background Color and Font Size

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
