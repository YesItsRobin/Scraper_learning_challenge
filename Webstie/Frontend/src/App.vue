<script>
import listItem from "./components/listItem.vue"
import axios from 'axios';

export default {
  data() {
    return {
      response: null,
      rerender: 0,
      filter: 'popularity',
      search: '',
    }
  },
  components: {
    listItem
  },
  methods: {
    searchSubmit() {
      axios.create({baseURL: "http://localhost:8000/", timeout: 20000}).post("?search=" +this.search +"&amount=12" +"&sort=" +this.filter).then(response => {
        this.response = response.data
        this.$forceUpdate()
        console.log(this.response)
      }).catch(error => {
        console.log(error)
      })
    },
    changeFilter(newFilter) {
      this.filter = newFilter
      this.rerender++
    }
  }
}
</script>

<template>
  <div class="main m-auto" :key="this.rerender">
    <header>
      <div>
        <h1 class="fixed-top p-4">
          <img width="70" class="img" src="./assets/logo.jpeg">
          Boller.com
        </h1>
      </div>
      <div class="container search-container">
        <div class="row">
          <div class="col-8 input-group">
            <input class="form-control search-bar float-left w-50" v-model="search" placeholder="Search...."/>
            <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown">
              {{ this.filter }} 
            </button>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" @click="changeFilter('popularity')">popularity</a></li>
              <li><a class="dropdown-item" @click="changeFilter('price low to high')">price low to high</a></li>
              <li><a class="dropdown-item" @click="changeFilter('price hight to low')">price hight to low</a></li>
              <li><a class="dropdown-item" @click="changeFilter('realease date')">realease date</a></li>
              <li><a class="dropdown-item" @click="changeFilter('most wanted')">Most wanted</a></li>
            </ul>
          </div>
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
          :item-link="item.href"
          :name="item.title"
          :price="item.price"
          :description="item.description"
          class="card mt-3 align-self-star"
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

.input-group {
  width: 40vw !important;
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
