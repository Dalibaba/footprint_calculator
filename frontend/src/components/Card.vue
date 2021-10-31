<template>
<div class="card">
  <div class="card-header">
    {{data.type}}
  </div>
  <div class="card-body">
    <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Distance</th>
              <th scope="col">Duration</th>
              <th scope="col">Footprint</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{{ data.distance }}</td>
              <td>{{ data.duration }}</td>
              <td>{{ data.footprint }}</td>
            </tr>
          </tbody>
        </table>

  <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
  <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
</template>

<script>
export default {
  name: "Card",
  props: {
    data: Object,
  },
};
</script>
