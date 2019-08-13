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
    background-image url("data:image/svg+xml,%3Csvg version='1.1' id='Calque_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 199 96' style='enable-background:new 0 0 199 96;' xml:space='preserve'%3E%3Cstyle type='text/css'%3E .st0%7Bfill:%23E30613;%7D .st1%7Bfill:%23FFFFFF;%7D%0A%3C/style%3E%3Cg id='Logo'%3E%3Cpolygon id='Fill-1' class='st0' points='0,0 0,96 199,96 199,0'/%3E%3Cg id='heig-vd' transform='translate(31.609060, 15.219177)'%3E%3Cpath id='Fill-2' class='st1' d='M7.7,59.9V39.2c0-4.6-0.7-9.5-7.7-9.5c-2.6,0-4.2,0.7-5.4,1.7c-2.3,2-2.8,5.3-2.8,7.6v20.9 h-3.4V16.6h3.4v15.5c0.4-1.7,3.2-5.3,8.8-5.3c4.3,0,7.4,1.6,8.7,3.7c1.6,2.3,1.8,5,1.8,8.6v20.9H7.7z'/%3E%3Cpath id='Fill-4' class='st1' d='M29.4,29.6C20.1,29.5,20,41,20,41.7h18.3C38.3,41.7,38.5,29.8,29.4,29.6L29.4,29.6z M19.8,44.6v1.1c0.2,3,1,11.3,11.4,11.3c6.3,0,9.6-4.5,9.6-4.5l-0.4,4.2c0,0-3.2,3.4-9.2,3.4c-13.8,0-14.8-11.4-14.8-16.4 c0-5.2,1.5-17,13.1-17.1C41.1,26.7,41.7,39.6,41.7,43v1.6H19.8z'/%3E%3Cpolygon id='Fill-6' class='st1' points='85.4,46.3 85.4,43 99.1,43 99.1,46.3'/%3E%3Cpath id='Fill-8' class='st1' d='M148.2,39.5c0-1.6-0.3-5.4-2.1-7.4c-1.2-1.4-3.3-2.4-6-2.4c-5.9,0-9.2,6.3-9.2,13.9 c0.1,7.4,2.7,13.9,9.2,13.9c5.4,0,8.1-4.5,8.1-8.5V39.5z M139.6,60.4c-8.6,0-12.3-7.7-12.3-17c0-9.1,4.9-16.6,12.5-16.5 c5.4,0.1,8,3.3,8.3,4.7v-15h3.4v31.8C151.6,52.8,148.9,60.4,139.6,60.4L139.6,60.4z'/%3E%3Cpath id='Fill-9' class='st1' d='M122.5,27.5c0,0-8.8,28.1-8.9,28.4c-0.2,0.5-0.3,0.5-0.4,0c-0.1-0.3-8.9-28.3-8.9-28.3h-3.5 l9.6,30.3c0.7,1.7,1.6,2.4,3,2.4c1.4,0,2.3-0.7,3-2.4l9.6-30.3H122.5z'/%3E%3Cpolygon id='Fill-10' class='st1' points='47.4,59.9 47.4,27.5 50.8,27.5 50.8,59.9'/%3E%3Cpolygon id='Fill-11' class='st1' points='47.4,22.3 47.4,18.8 50.9,18.8 50.9,22.3'/%3E%3Cpath id='Fill-12' class='st1' d='M69.5,68.3c-6.1,0-9.5-2.5-9.5-6c0-2.7,2.3-5,4.1-5.4c0,0,2.9-0.1,5.4,0 c6.9,0.1,8.9,2.6,8.9,5.4C78.4,66.3,73.8,68.3,69.5,68.3 M61.4,38c0-4.8,2.3-8.3,8-8.3c6.1,0,8.2,4.3,8.2,8.3 c0,5.5-3.5,8.3-8.4,8.3C64.7,46.2,61.4,42.9,61.4,38 M69.8,53.7c-3.1,0-9.6,0.8-9.6-2.4c0-2.8,4.6-2.5,9.1-2.5 c7.1,0,11.4-4.2,11.4-10.9c0-3.5-1.2-6.4-3.4-8.4h3.8v-2.9h-12v0c-0.1,0-0.1,0-0.2,0c-5.1,0-10.7,2.8-10.7,11.2 c0,5.6,3.7,8.5,5.1,8.7c-1.4,0-6.3,0.7-6.2,5.2c0.1,2.5,1.4,3.7,4.1,4.2c-1.6,0.5-4.3,3-4.3,6.8c0,4.6,4.2,8.3,12.6,8.3 c6.9,0,12.1-3,12.2-8.9C81.8,56.7,78.1,53.7,69.8,53.7'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E%0A")
    width 8em
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
