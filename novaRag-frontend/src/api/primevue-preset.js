import { definePreset } from '@primevue/themes'
import Aura from '@primevue/themes/aura'

// novaRAG maps its five accent shades onto PrimeVue's 13-step palette scale.
// PrimeVue components read color via these semantic tokens, so theming happens
// once, here, rather than per-component with Tailwind overrides scattered around.
const novaRagPreset = definePreset(Aura, {
  semantic: {
    primary: {
      50: '#FBF3F0',
      100: '#F3DCE1',
      200: '#EBC8D1', // soft pink
      300: '#C98A9B',
      400: '#9A4F5F',
      500: '#7A3043', // secondary accent
      600: '#5A1F2D', // primary accent
      700: '#4A1925',
      800: '#3A131D',
      900: '#2A0D15',
      950: '#1A0810',
    },
    focusRing: {
      width: '2px',
      style: 'solid',
      color: '#7A3043',
      offset: '2px',
    },
    borderRadius: {
      xs: '6px',
      sm: '10px',
      md: '14px',
      lg: '20px',
      xl: '28px',
    },
    colorScheme: {
      light: {
        surface: {
          0: '#FFFFFF',
          50: '#F7F1EC',
          100: '#F3E7E1',
          200: '#EBDCD4',
          300: '#D8C8C2',
          400: '#C4B2AB',
          500: '#A99089',
          600: '#8A736D',
          700: '#6F6F6F',
          800: '#4A3A38',
          900: '#2B2B2B',
          950: '#1C1414',
        },
        primary: {
          color: '#5A1F2D',
          contrastColor: '#FFFFFF',
          hoverColor: '#7A3043',
          activeColor: '#4A1925',
        },
        highlight: {
          background: '#EBC8D1',
          focusBackground: '#E3B9C4',
          color: '#5A1F2D',
          focusColor: '#5A1F2D',
        },
        text: {
          color: '#2B2B2B',
          hoverColor: '#2B2B2B',
          mutedColor: '#6F6F6F',
        },
        content: {
          background: '#FFFFFF',
          hoverBackground: '#F7F1EC',
          borderColor: '#D8C8C2',
        },
        formField: {
          background: '#FFFFFF',
          borderColor: '#D8C8C2',
          hoverBorderColor: '#7A3043',
          focusBorderColor: '#5A1F2D',
        },
      },
    },
  },
  components: {
    card: {
      colorScheme: {
        light: {
          root: {
            background: '#FFFFFF',
            borderRadius: '20px',
            shadow: '0 1px 2px rgba(43,27,27,0.04), 0 8px 24px -12px rgba(90,31,45,0.12)',
          },
        },
      },
    },
    button: {
      root: {
        borderRadius: '10px',
        fontWeight: '600',
        transitionDuration: '200ms',
      },
    },
    datatable: {
      colorScheme: {
        light: {
          headerCell: {
            background: '#F3E7E1',
            color: '#6F6F6F',
          },
          row: {
            hoverBackground: '#F7F1EC',
          },
        },
      },
    },
    tag: {
      root: {
        borderRadius: '999px',
        fontWeight: '600',
      },
    },
    toast: {
      root: {
        borderRadius: '14px',
      },
    },
  },
})

export default novaRagPreset