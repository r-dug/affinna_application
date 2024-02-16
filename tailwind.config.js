/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/*.{html,js}'],
  theme: {
    colors: {
      'blue': '#1fb6ff',
      'white': '#ffffff',
      'black': '#000000',
      'blue2': '#1e3dc5'
    },
    fontFamily: {
      sans: ['"Apple Color Emoji"'],
      serif: ['Merriweather', 'serif'],
      mono: ['"Liberation Mono"'],
    },
    extend: {
      keyframes: {
        wiggle: {
          '25%, 75%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
        colors: {
          "50%": { change: 'bg-blue2', change: 'text-white' },
          "50%": { change: 'bg-blue', change: 'text-black' },
          "100%": { change: 'bg-blue2', change: 'text-white' },
        }
      },

      animation: {
        colors: 'colors 3s ease-in-out infinite',
        wiggle: 'wiggle 1s ease-in-out infinite',
      },
      spacing: {
        '8xl': '96rem',
        '9xl': '128rem',
      },
      borderRadius: {
        '4xl': '2rem',
      }
    },
  plugins: [
  ],
  corePlugins: [
    'margin',
    'padding',
    'backgroundColor',
  ]
}
}
