<template>
  <li v-for="job in jobs" v-bind:key="job.id">
    <p>{{ job }}</p>
  </li>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      jobs: [],
    };
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get("http://localhost:8000/jobs");
        // JSON responses are automatically parsed.
        this.jobs = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>
