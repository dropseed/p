const purgecss = require('@fullhuman/postcss-purgecss')({
    content: [
        './output/**/*.html',
    ],

    // Include any special characters you're using in this regular expression
    defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
})

module.exports = {
    plugins: [
        require('tailwindcss')(__dirname + '/_tailwind.config.js'),
        require('autoprefixer'),
        process.env.CONTEXT == 'production' ? purgecss : null,
    ]
}
