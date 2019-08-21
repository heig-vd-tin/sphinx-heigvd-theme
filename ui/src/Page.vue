<template>
  <div class="page">
    <slot />

    <!-- <Content :custom="false"/> -->

    <!-- <div class="page-edit"> -->
    <!--   <div -->
    <!--     class="edit-link" -->
    <!--     v-if="editLink" -->
    <!--   > -->
    <!--     <a -->
    <!--       :href="editLink" -->
    <!--       target="_blank" -->
    <!--       rel="noopener noreferrer" -->
    <!--     >{{ editLinkText }}</a> -->
    <!--     <OutboundLink/> -->
    <!--   </div> -->

    <!--   <div -->
    <!--     class="last-updated" -->
    <!--     v-if="lastUpdated" -->
    <!--   > -->
    <!--     <span class="prefix">{{ lastUpdatedText }}: </span> -->
    <!--     <span class="time">{{ lastUpdated }}</span> -->
    <!--   </div> -->
    <!-- </div> -->

    <!-- <div class="page-nav" v-if="prev || next"> -->
    <!--   <p class="inner"> -->
    <!--     <span -->
    <!--       v-if="prev" -->
    <!--       class="prev" -->
    <!--     > -->
    <!--       ← -->
    <!--       <router-link -->
    <!--         v-if="prev" -->
    <!--         class="prev" -->
    <!--         :to="prev.path" -->
    <!--       > -->
    <!--         {{ prev.title || prev.path }} -->
    <!--       </router-link> -->
    <!--     </span> -->

    <!--     <span -->
    <!--       v-if="next" -->
    <!--       class="next" -->
    <!--     > -->
    <!--       <router-link -->
    <!--         v-if="next" -->
    <!--         :to="next.path" -->
    <!--       > -->
    <!--         {{ next.title || next.path }} -->
    <!--       </router-link> -->
    <!--       → -->
    <!--     </span> -->
    <!--   </p> -->
    <!-- </div> -->

    <slot name="bottom" />
  </div>
</template>

<script>
//import { resolvePage, normalize, outboundRE, endingSlashRE } from './util'
import JQuery from "jquery";
import Clipboard from 'clipboard'

var $ = JQuery;

export default {
  /*
  props: ['sidebarItems'],

  computed: {
    lastUpdated () {
      if (this.$page.lastUpdated) {
        return new Date(this.$page.lastUpdated).toLocaleString(this.$lang)
      }
    },

    lastUpdatedText () {
      if (typeof this.$themeLocaleConfig.lastUpdated === 'string') {
        return this.$themeLocaleConfig.lastUpdated
      }
      if (typeof this.$site.themeConfig.lastUpdated === 'string') {
        return this.$site.themeConfig.lastUpdated
      }
      return 'Last Updated'
    },

    prev () {
      const prev = this.$page.frontmatter.prev
      if (prev === false) {
        return
      } else if (prev) {
        return resolvePage(this.$site.pages, prev, this.$route.path)
      } else {
        return resolvePrev(this.$page, this.sidebarItems)
      }
    },

    next () {
      const next = this.$page.frontmatter.next
      if (next === false) {
        return
      } else if (next) {
        return resolvePage(this.$site.pages, next, this.$route.path)
      } else {
        return resolveNext(this.$page, this.sidebarItems)
      }
    },

    editLink () {
      if (this.$page.frontmatter.editLink === false) {
        return
      }
      const {
        repo,
        editLinks,
        docsDir = '',
        docsBranch = 'master',
        docsRepo = repo
      } = this.$site.themeConfig

      let path = normalize(this.$page.path)
      if (endingSlashRE.test(path)) {
        path += 'README.md'
      } else {
        path += '.md'
      }
      if (docsRepo && editLinks) {
        return this.createEditLink(repo, docsRepo, docsDir, docsBranch, path)
      }
    },

    editLinkText () {
      return (
        this.$themeLocaleConfig.editLinkText ||
        this.$site.themeConfig.editLinkText ||
        `Edit this page`
      )
    }
  },

  methods: {
    createEditLink (repo, docsRepo, docsDir, docsBranch, path) {
      const bitbucket = /bitbucket.org/
      if (bitbucket.test(repo)) {
        const base = outboundRE.test(docsRepo)
          ? docsRepo
          : repo
        return (
          base.replace(endingSlashRE, '') +
           `/${docsBranch}` +
           (docsDir ? '/' + docsDir.replace(endingSlashRE, '') : '') +
           path +
           `?mode=edit&spa=0&at=${docsBranch}&fileviewer=file-view-default`
        )
      }

      const base = outboundRE.test(docsRepo)
        ? docsRepo
        : `https://github.com/${docsRepo}`

      return (
        base.replace(endingSlashRE, '') +
        `/edit/${docsBranch}` +
        (docsDir ? '/' + docsDir.replace(endingSlashRE, '') : '') +
        path
      )
    }
  }
  */
};
/*
function resolvePrev (page, items) {
  return find(page, items, -1)
}

function resolveNext (page, items) {
  return find(page, items, 1)
}

function find (page, items, offset) {
  const res = []
  items.forEach(item => {
    if (item.type === 'group') {
      res.push(...item.children || [])
    } else {
      res.push(item)
    }
  })
  for (let i = 0; i < res.length; i++) {
    const cur = res[i]
    if (cur.type === 'page' && cur.path === page.path) {
      return res[i + offset]
    }
  }
}
*/

$(document).ready(function() {
  $(".solution .admonition-title").click(function() {
    $(this)
      .parent()
      .toggleClass("open");
  });
});

function addCopyButtonToCode() {
  // get all code elements
  var allCodeBlocksElements = $("div.highlight pre");

  // For each element, do the following steps
  allCodeBlocksElements.each(function(ii) {
    // define a unique id for this element and add it
    var currentId = "codeblock" + (ii + 1);
    $(this).attr("id", currentId);

    // create a button that's configured for clipboard.js
    // point it to the text that's in this code block
    // add the button just after the text in the code block w/ jquery
    var clipButton =
      '<button class="btn copybtn" data-clipboard-target="#' +
      currentId +
      '"><img src="https://clipboardjs.com/assets/images/clippy.svg" width="13" alt="Copy to clipboard"></button>';
    $(this).after(clipButton);
  });

  // tell clipboard.js to look for clicks that match this query
  new Clipboard(".btn");
}

$(document).ready(function() {
  // Once the DOM is loaded for the page, attach clipboard buttons
  addCopyButtonToCode();
});
</script>

<style lang="stylus">
@import './vuepress/styles/config.styl';
@require './vuepress/styles/wrapper.styl';

.page {
  padding-top: $navbarHeight;
  padding-bottom: 2rem;
}

.page-edit {
  @extend $wrapper;
  padding-top: 1rem;
  padding-bottom: 1rem;
  overflow: auto;

  .edit-link {
    display: inline-block;

    a {
      color: lighten($textColor, 25%);
      margin-right: 0.25rem;
    }
  }

  .last-updated {
    float: right;
    font-size: 0.9em;

    .prefix {
      font-weight: 500;
      color: lighten($textColor, 25%);
    }

    .time {
      font-weight: 400;
      color: #aaa;
    }
  }
}

.page-nav {
  @extend $wrapper;
  padding-top: 1rem;
  padding-bottom: 0;

  .inner {
    min-height: 2rem;
    margin-top: 0;
    border-top: 1px solid $borderColor;
    padding-top: 1rem;
    overflow: auto; // clear float
  }

  .next {
    float: right;
  }
}

@media (max-width: $MQMobile) {
  .page-edit {
    .edit-link {
      margin-bottom: 0.5rem;
    }

    .last-updated {
      font-size: 0.8em;
      float: none;
      text-align: left;
    }
  }
}
</style>
