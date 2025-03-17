import gradio as gr

def predict_price(zimmeranzahl, wohnfläche, ausländeranteil):
    return f"Die geschätzte Miete beträgt: {zimmeranzahl * wohnfläche * (1 + ausländeranteil * 0.01)} CHF"

demo = gr.Interface(
    fn=predict_price,
    inputs=["number", "number", "number"],
    outputs="text",
    title="Mietpreis Vorhersage",
)

demo.launch()
