<template>
<header class="navbar">
  <SidebarButton @toggle-sidebar="$emit('toggle-sidebar')"/>
  <div class="logo"></div>
  <slot></slot>

    <!--   <img -->
    <!--     class="logo" -->
    <!--     v-if="$site.themeConfig.logo" -->
    <!--     :src="$withBase($site.themeConfig.logo)" -->
    <!--     :alt="$siteTitle" -->
    <!--   > -->
    <!--   <span -->
    <!--     class="site-name" -->
    <!--     v-if="$siteTitle" -->
    <!--     :class="{ 'can-hide': $site.themeConfig.logo }" -->
    <!--   >{{ $siteTitle }}</span> -->
    <!-- </router-link> -->

    <!-- <div class="links"> -->
    <!--   <AlgoliaSearchBox -->
    <!--     v-if="isAlgoliaSearch" -->
    <!--     :options="algolia" -->
    <!--   /> -->
    <!--   <SearchBox v-else-if="$site.themeConfig.search !== false"/> -->
    <!-- </div> -->
</header>
</template>

<script>
import SidebarButton from './vuepress/SidebarButton.vue'
// import AlgoliaSearchBox from '@AlgoliaSearchBox'
// import SearchBox from './SearchBox.vue'
// import NavLinks from './NavLinks.vue'

export default {
  components: { SidebarButton }, // NavLinks, SearchBox, AlgoliaSearchBox },

//   computed: {
//     algolia () {
//       return this.$themeLocaleConfig.algolia || this.$site.themeConfig.algolia || {}
//     },

//     isAlgoliaSearch () {
//       return this.algolia && this.algolia.apiKey && this.algolia.indexName
//     }
//   }
}
</script>

<style lang="stylus">

@import './vuepress/styles/config.styl'

.navbar
  padding 0
  line-height $navbarHeight - 1.4rem
  position fixed // relative
  a, span, img
    display inline-block
  .logo
    background-image url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTMuMDMgMTAyLjUyIj48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2U1M2MzMDt9LmNscy0ye2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PGcgaWQ9IkxheWVyXzIiIGRhdGEtbmFtZT0iTGF5ZXIgMiI+PGcgaWQ9IkxheWVyXzEtMiIgZGF0YS1uYW1lPSJMYXllciAxIj48cmVjdCBjbGFzcz0iY2xzLTEiIHdpZHRoPSIyNTMuMDMiIGhlaWdodD0iMTAyLjUyIi8+PHBhdGggY2xhc3M9ImNscy0yIiBkPSJNOTYsNzQuNUg3NS4zM3Y2LjMySDg5LjY4bDAsLjM0Yy0xLjkzLDUuNTEtNi4zNiw4LjY4LTEzLjM2LDguNjgtOC4wNywwLTE0LjE3LTYuNDctMTQuMTctMTQuNjZDNjIuMTcsNjYuNjcsNjguNTEsNjAsNzYuOTMsNjBjNi40NCwwLDExLDMuMTYsMTMuNjQsOC44Mkw5Ni41MSw2NmMtMy42Ny03Ljk0LTEwLjYyLTEyLjMxLTE5LjU4LTEyLjMxQTIxLjE0LDIxLjE0LDAsMCwwLDU1LjY1LDc1LjE5YTIwLjU4LDIwLjU4LDAsMCwwLDIwLjcsMjAuOSwxNy43MiwxNy43MiwwLDAsMCwxMy45My02LjI2bC41OSw0Ljc2SDk2Vjc0LjVaIi8+PHBvbHlnb24gY2xhc3M9ImNscy0yIiBwb2ludHM9Ijk2LjAxIDQwLjI0IDYzLjMgNDAuMjQgNjMuMyAyOS44IDkyLjI1IDI5LjggOTIuMjUgMjMuNzQgNjMuMyAyMy43NCA2My4zIDEzLjMgOTYuMDEgMTMuMyA5Ni4wMSA3LjA4IDU2LjYzIDcuMDggNTYuNjMgNDYuNDUgOTYuMDEgNDYuNDUgOTYuMDEgNDAuMjQiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iNDEuMTYgMjMuMzUgMTUuMTcgMjMuMzUgMTUuMTcgNy4wOCA4LjUxIDcuMDggOC41MSA0Ni40NSAxNS4xNyA0Ni40NSAxNS4xNyAyOS42MyA0MS4xNiAyOS42MyA0MS4xNiA0Ni40NSA0Ny44OSA0Ni40NSA0Ny44OSA3LjA4IDQxLjE2IDcuMDggNDEuMTYgMjMuMzUiLz48cG9seWdvbiBjbGFzcz0iY2xzLTIiIHBvaW50cz0iMzEuNTMgODguMzEgMzEuNTMgNjEuNDggNDcuODkgNjEuNDggNDcuODkgNTUuMjEgOC41MSA1NS4yMSA4LjUxIDYxLjQ4IDI0Ljg2IDYxLjQ4IDI0Ljg2IDg4LjMxIDguNTEgODguMzEgOC41MSA5NC41OSA0Ny44OSA5NC41OSA0Ny44OSA4OC4zMSAzMS41MyA4OC4zMSIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTExMi41Miw3LjA1aDIuNTNsLTMuOTEsMTAuN2gtMi40NWwtMy45Mi0xMC43aDIuNjJMMTEwLDE0LjU3WiIvPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTExNy4yNywxNy43NVY3LjA1aDMuODhhNSw1LDAsMCwxLDUuMzcsNS4zNiw1LDUsMCwwLDEtNS4zOSw1LjM0Wm0zLjc4LTIuMjVhMi44LDIuOCwwLDAsMCwzLTMuMDksMi44MSwyLjgxLDAsMCwwLTMtMy4xMWgtMS4zOXY2LjJaIi8+PC9nPjwvZz48L3N2Zz4=')
    background-repeat: no-repeat;
    width 9em
    height 3.5em
    height $navbarHeight
    min-width $navbarHeight
    margin-right 0.8rem
    vertical-align top
  .site-name
    font-size 1.3rem
    font-weight 600
    color $textColor
    position relative
  .links
    font-size 0.9rem
    position absolute
    right 1.5rem
    top 0.7rem

@media (max-width: $MQMobile)
  .navbar
    padding-left 4rem
    .can-hide
      display none
</style>
