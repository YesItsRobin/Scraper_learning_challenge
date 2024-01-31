<script>
import listItem from "./components/listItem.vue"

export default {
  data() {
    search: String
  },
  components: {
    listItem
  },
  methods: {
    searchSubmit() {
      if (this.search == undefined) {
        return;
      }

      console.log(this.search)
    }
  }
}
</script>

<template>
  <div class="w-50 m-auto">
    <header>
      <div>
        <h1 class="fixed-top p-4">
          Boller.com
        </h1>
      </div>
      <div class="container search-container">
        <div class="row">
          <input class="form-control search-bar float-left col-8" v-model="search" placeholder="Search...."/>
          <div class="col"></div>
          <button class="btn btn-primary float-right col-4 ml-2" @click="searchSubmit">Search</button>
        </div>
      </div>
    </header>
    <main>
      <div class="mt-5 p-2">
        <div>
          <list-item msg="this item"></list-item>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.search-bar {
  width: 60%;
  height: 60px;
}

.search-container {
  margin-top: 125px;
}
</style>
