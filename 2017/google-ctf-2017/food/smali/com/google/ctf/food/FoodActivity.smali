.class public Lcom/google/ctf/food/FoodActivity;
.super Landroid/support/v7/app/AppCompatActivity;
.source "FoodActivity.java"


# static fields
.field public static activity:Landroid/app/Activity;


# direct methods
.method public constructor <init>()V
    .locals 0

    .prologue
    .line 7
    invoke-direct {p0}, Landroid/support/v7/app/AppCompatActivity;-><init>()V

    return-void
.end method


# virtual methods
.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1
    .param p1, "savedInstanceState"    # Landroid/os/Bundle;

    .prologue
    .line 13
    invoke-super {p0, p1}, Landroid/support/v7/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    .line 14
    const v0, 0x7f040019

    invoke-virtual {p0, v0}, Lcom/google/ctf/food/FoodActivity;->setContentView(I)V

    .line 15
    sput-object p0, Lcom/google/ctf/food/FoodActivity;->activity:Landroid/app/Activity;

    .line 16
    const-string v0, "cook"

    invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

    .line 17
    return-void
.end method
