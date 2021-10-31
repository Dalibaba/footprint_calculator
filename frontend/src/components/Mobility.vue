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
    <button type="button" class="btn btn-success btn-sm" @click="onClickCalculate">Calculate</button>
  <ul style="list-style-type:none;"> 
    <li v-for="item in options" :key="item.type">
      <Card :data="item"/>
    </li>
  </ul>
  <div>
    <p>{{ this.duration }}</p>
  </div>
  </div>
</template>

<script>

import axios from 'axios';
import Card from './Card.vue'
export default {
  name: 'Mobility',
  components: {
    Card
  },
  data() {
    return {
      start: '',
      destination: '',
      duration: '',
      options: [
        {type: "car", distance: 213, duration: 23, footprint: 12},
        {type: "train", distance: 23, duration: 12, footprint: 4},
      ]
    };
  },
  methods: {
    onClickCalculate() {
      const path = 'http://localhost:8000/mobility';
      axios.get(path, { params: {
  start: this.start,
  destination: this.destination
}})
        .then((res) => {
          this.duration = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      
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

