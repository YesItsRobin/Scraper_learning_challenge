<template>
    <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title fs-6 text">
                {{ name }}
                
            </h5>
            <div>
                <p class="card-text">{{ description }}</p>
                <hr>
                <span class="float-end text-primary">{{ price }}</span>
                <a :href="itemLink" class="btn btn-primary">Go to item</a>
            </div>
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
        description: String,
    }
}
</script>

<style scoped>
.card-img-top {
    height: 200px;
    width: auto;
    overflow: hidden;
}

.btn {
    
}
</style>