import { Card, CardActionArea, CardMedia, Typography } from "@mui/material";

const MovCard = ({ imageSrc, title }) => {
  return (
    <Card sx={{ maxWidth: 150, padding: "2px", borderRadius: "20px" }}>
      <CardActionArea>
        <CardMedia component="img" height="200" image={imageSrc} alt={title} />
        <Typography variant="h4" align="center">
          {title}
        </Typography>
      </CardActionArea>
    </Card>
  );
};

export default MovCard;
