FROM golang:1.22-alpine AS builder

RUN apk add --no-cache 
WORKDIR /app
COPY go.mod ./ 
RUN go mod download
COPY . .

RUN go build -o redirector
EXPOSE 8000

FROM alpine

WORKDIR /app 
COPY --from=builder /app/redirector /app/

CMD ["/app/redirector"]

