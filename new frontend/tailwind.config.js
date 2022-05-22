module.exports = {
    mode: 'jit',
    purge: ['./src/**/*.js', './public/index.html'],
    darkMode: "class", // or 'media' or 'class'
    theme: {
        fontFamily: {
            sans: ['Roboto', 'sans-serif'],
            serif: ['"Roboto Slab"', 'serif'],
            body: ['Roboto', 'sans-serif'],
        },
        extend: {
            backgroundImage: () => ({
                'profile-background':
                    "linear-gradient(rgba(0,0,0, 0.25), rgba(0,0,0, 0.25))",
            }),
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
};
