<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Mobility</h1>
        <hr />
      </div>
    </div>
  <div class="form-group">

        <input
          type="text"
          v-model="start"
          class="form-control"
          id="startInput"
          placeholder="Start"
        />
  </div>
  <div class="form-group">
        <input
          type="text"
          v-model="destination"
          class="form-control"
          id="destinationInput"
          placeholder="Destination"
        />
  </div>
  <div class="container">
      <div class="row justify-content-center">
         <button type="button" class="btn btn-success btn-sm" @click="onClickCalculate">Calculate</button>
      </div>
   
  </div>
  <div v-if="loading">
    <div class="container">
      <div class="row justify-content-center">
          <ring-loader :loading="loading" :color="color1" :size="size"></ring-loader>
      </div>
  </div>
  </div>
  <div v-else>
  <ul style="list-style-type:none;"> 
    <li v-for="(item, index) in options" :key="item.duration">
      <Card :data="item" :type="index"/>
    </li>
  </ul>
  <div class="row justify-content-center">
      <p>{{this.errorMessage}}</p>
  </div>

  </div>
  </div>
</template>

<script>

import axios from 'axios';
import Card from './Card.vue'
import RingLoader from 'vue-spinner/src/RingLoader.vue'
export default {
  name: 'Mobility',
  components: {
    Card,
    RingLoader,
  },
  data() {
    return {
      start: '',
      destination: '',
      options: '',
      loading: false,
      errorMessage: ''
    };
  },
  methods: {
    onClickCalculate() {
      this.options = '';
      this.errorMessage = '';
      this.loading = true;
      const path = 'http://localhost:8000/mobility';
      axios.get(path, { params: {
  start: this.start,
  destination: this.destination
}})
        .then((res) => {
          this.options = res.data;
          
        })
        .catch(() => {
          this.errorMessage = "variables can't be read"
        })
        .finally(() => (this.loading = false)) // set loading to false when request finish;
      
    },
  },
};
</script>

<style>
ul {
    list-style: none;
    padding-left: 0;
};
</style>

