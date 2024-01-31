<template>
    <div class="card" style="width: 18rem;">
        <img :src="imagePath" class="card-img-top p-4">
        <div class="card-body">
            <h5 class="card-title fs-6 text">
                {{ name }}
                <span class="float-end text-primary">{{ price }}</span>
            </h5>
            <hr>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a :href="itemLink" class="btn btn-primary float-end">Go to item</a>
    </div>
</div>
</template>

<script>

export default {
    props: {
        imagePath: String,
        itemLink: String,
        name: String,
        price: String,
    }
}
</script>

<style scoped>
.card-img-top {
    height: 200px;
    width: auto;
    overflow: hidden;
}

</style>