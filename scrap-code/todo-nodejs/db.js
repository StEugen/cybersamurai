const knex = require('knex');

const db = kenx({
    client: "pg",
    connection: process.env.POSTGRESQL_URL
})

module.exports = { db }