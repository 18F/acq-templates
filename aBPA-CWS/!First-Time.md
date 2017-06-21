# How to...
## Make paragraphs in your variables

This is a template that will attempt to show you how to add paragraphs when filling out the various fields on your form.

Watch in between this line to see what happens:

----------

{{askBackground}}

----------

In the box on the left, find (CTRL+F or CMD+F) the variable `askBackground`.

**Note, when you copy the examples, the space between the `:` and the `"` will sometimes disappear. You need that space.**

In between the two quotation marks, type in two sentences you want to show up as paragraphs. Example:

`askBackground: "I want to buy something. I want to be joyful when I buy it."`

In between the two sentences, specifically, the space between the `.` and the `I`, put in `\r\r` so it looks like this:

`askBackground: "I want to buy something.\r\rI want to be joyful when I buy it."`

Add an `\r\r` for each paragraph. For example:

`askBackground: "I want to buy something.\r\rI want to be joyful when I buy it.\r\rIn fact, I want to be moved to throw a parade."`

## Make bullet points

After the `\r\r`, put a `+` sign and then a space with the bullet. Example:

`askBackground: "line 1\r\rline 2\r\r+ bullet 1\r\r+bullet 2"`

## LifeProTip

Take your paragraphs and put it into a program like Sublime Text, Atom, or even a separate Google Doc. Do a "Find and replace" for `. ` and replace it with a `.\r\r`. That should capture most of your line breaks.
