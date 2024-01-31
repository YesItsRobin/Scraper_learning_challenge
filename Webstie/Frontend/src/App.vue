<script>
import listItem from "./components/listItem.vue"
import axios from 'axios';

export default {
  data() {
    response: null
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
      console.log(this.response)
      axios.create({baseURL: "http://localhost:8000/", timeout: 5000}).post("?search=" +this.search).then(response => {
        this.response = response.data
        this.$forceUpdate()
        console.log(this.response)
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<template>
  <div class="main m-auto">
    <header>
      <div>
        <h1 class="fixed-top p-4">
          <img width="70" class="img" src="./assets/logo.webp">
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
      <div class="d-flex flex-wrap justify-content-evenly mt-4 mb-5">
        <list-item 
          v-for="(item, index) in this.response"
          :image-path="item.image"
          item-link="https://www.bol.com/nl/nl/p/lg-32lq63006la-32-inch-full-hd-led-2022/9300000074859721/?bltgh=salXVqHQPv58dV9OcyRMxA.4_29.35.ProductTitle"
          name="LG 32LQ63006LA - 32 inch - Full HD LED - 2022"
          price="€229,95"
          class="card mt-3"
          :key="index"
        ></list-item>
      </div>
    </main>
  </div>
</template>

<style scoped>
.search-bar {
  width: 60%;
  height: 60px;
  border-width: 2px;
  font-size: 18px;
  padding-left: 20px;
}

.btn {
  font-size: 18px;
}

.search-container {
  margin-top: 125px;
}

.img {
  margin-top: -9px;
}

.main {
  width: 65vw !important;
}
</style>
